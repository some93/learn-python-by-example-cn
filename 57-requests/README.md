# 第 57 关：requests（师兄带你学 Python）

## 🎯 这一关你会学到

- 用 `requests.get()` 发送 GET 请求
- 用 `params` 传查询参数
- 用 `requests.post()` 发送表单和 JSON
- 读取 `status_code`、响应头、响应 JSON
- 设置请求头和超时时间
- 用 `Session` 自动保持 Cookie
- 用 `raise_for_status()` 处理 HTTP 错误

## 🤔 先想一个问题

你要调用一个接口：带参数查用户、POST 创建订单、设置请求头、登录后保持 Cookie。标准库也能做，但写起来偏底层。

`requests` 的目标是让 HTTP 请求更直观。不过它是第三方库，使用前需要安装：

```bash
python -m pip install requests
```

这一章为了保证离线也能运行，会在本机临时启动一个小 HTTP 服务，再用 `requests` 去访问它。

## 📖 看代码

```python
# requests HTTP 客户端

import json
import threading
from http.cookies import SimpleCookie
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qs, urlparse

import requests


class DemoAPI(BaseHTTPRequestHandler):
    def _send_json(self, payload, status=200, headers=None):
        # 本地演示 API 统一返回 JSON，方便 requests 调用 response.json()。
        body = json.dumps(payload, ensure_ascii=False).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        for key, value in (headers or {}).items():
            self.send_header(key, value)
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, format, *args):
        # 关闭 http.server 默认访问日志，让教程输出更干净。
        return

    def do_GET(self):
        # BaseHTTPRequestHandler 会把请求路径放在 self.path。
        parsed = urlparse(self.path)

        if parsed.path == "/api/hello":
            # parse_qs 会把查询参数解析成 key -> list 的形式。
            query = parse_qs(parsed.query)
            name = query.get("name", ["Python"])[0]
            self._send_json({"message": f"Hello, {name}", "query": query})
            return

        if parsed.path == "/api/headers":
            self._send_json({"user_agent": self.headers.get("User-Agent")})
            return

        if parsed.path == "/api/set-cookie":
            # Set-Cookie 响应头会被 requests.Session 自动保存。
            self._send_json({"ok": True}, headers={"Set-Cookie": "token=abc123; Path=/"})
            return

        if parsed.path == "/api/cookies":
            # 下一次请求时，Session 会自动把 Cookie 带回来。
            cookie = SimpleCookie(self.headers.get("Cookie"))
            token = cookie.get("token")
            self._send_json({"token": token.value if token else None})
            return

        self._send_json({"error": "not found"}, status=404)

    def do_POST(self):
        parsed = urlparse(self.path)
        # POST 请求体需要按 Content-Length 指定的长度读取。
        length = int(self.headers.get("Content-Length", 0))
        raw_body = self.rfile.read(length)

        if parsed.path == "/api/users":
            content_type = self.headers.get("Content-Type", "")

            # requests.post(json=...) 会自动设置 Content-Type 并序列化 JSON。
            if "application/json" in content_type:
                data = json.loads(raw_body.decode("utf-8"))
            else:
                data = {key: values[0] for key, values in parse_qs(raw_body.decode()).items()}

            self._send_json({"received": data})
            return

        self._send_json({"error": "not found"}, status=404)


def start_server():
    # 端口传 0 表示让系统分配一个空闲端口，避免和本机已有服务冲突。
    server = HTTPServer(("127.0.0.1", 0), DemoAPI)
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    return server


def main():
    server = start_server()
    base_url = f"http://127.0.0.1:{server.server_port}"

    try:
        print("=== GET 请求和 params ===")
        # params 会被 requests 自动编码到 URL 查询字符串里。
        response = requests.get(f"{base_url}/api/hello", params={"name": "Alice"}, timeout=3)
        response.raise_for_status()
        print(response.status_code)
        print(response.headers["Content-Type"])
        print(response.json())

        print("\n=== POST 表单和 JSON ===")
        # data 发送表单，json 发送 JSON；两者的 Content-Type 不同。
        form_response = requests.post(f"{base_url}/api/users", data={"name": "Bob", "age": "20"}, timeout=3)
        json_response = requests.post(f"{base_url}/api/users", json={"name": "Charlie", "age": 21}, timeout=3)
        print(form_response.json())
        print(json_response.json())

        print("\n=== 自定义请求头 ===")
        # headers 参数可以覆盖或补充请求头。
        headers = {"User-Agent": "learn-python-demo/1.0"}
        header_response = requests.get(f"{base_url}/api/headers", headers=headers, timeout=3)
        print(header_response.json())

        print("\n=== Session 保持 Cookie ===")
        # Session 适合登录态、Cookie、连接复用等连续请求场景。
        session = requests.Session()
        session.get(f"{base_url}/api/set-cookie", timeout=3)
        cookie_response = session.get(f"{base_url}/api/cookies", timeout=3)
        print(cookie_response.json())

        print("\n=== HTTP 错误处理 ===")
        # requests 默认不会因为 404 抛异常，需要主动调用 raise_for_status。
        not_found = requests.get(f"{base_url}/missing", timeout=3)
        try:
            not_found.raise_for_status()
        except requests.HTTPError as error:
            print(type(error).__name__)
            print(not_found.status_code)
    finally:
        # 本地演示服务用完要关闭，避免后台线程继续占用端口。
        server.shutdown()
        server.server_close()


if __name__ == "__main__":
    main()
```

## 🔍 师兄给你拆开讲

`requests.get(url, params=...)` 会把参数自动拼到 URL 查询字符串里，并处理必要的转义。不要自己手动拼复杂 URL。

`response.status_code` 是 HTTP 状态码，`response.headers` 是响应头，`response.text` 是文本内容，`response.content` 是二进制内容，`response.json()` 会把 JSON 响应解析成 Python 对象。

`requests.post(..., data=...)` 发送表单数据，`requests.post(..., json=...)` 发送 JSON。后者会自动设置 `Content-Type: application/json` 并序列化字典。

请求一定要写 `timeout`。不写超时，网络异常时程序可能卡住很久。

`Session` 会在多次请求之间保留 Cookie、连接池和默认配置，适合登录后连续访问接口。

`raise_for_status()` 会在 4xx / 5xx 响应时抛出 `HTTPError`。这样你不用每次手动判断状态码。

## 🏃 跑一下试试

```bash
cd 57-requests
python requests_demo.py
```

输出：

```text
=== GET 请求和 params ===
200
application/json; charset=utf-8
{'message': 'Hello, Alice', 'query': {'name': ['Alice']}}

=== POST 表单和 JSON ===
{'received': {'name': 'Bob', 'age': '20'}}
{'received': {'name': 'Charlie', 'age': 21}}

=== 自定义请求头 ===
{'user_agent': 'learn-python-demo/1.0'}

=== Session 保持 Cookie ===
{'token': 'abc123'}

=== HTTP 错误处理 ===
HTTPError
404
```

## 💡 师兄的提醒

`requests` 适合同步脚本、后台任务、小工具。如果你要写高并发异步 HTTP 客户端，通常会看 `httpx` 或 `aiohttp`。

爬网页时要遵守 robots、服务条款和频率限制。接口调用要处理超时、重试、鉴权、状态码和错误响应，不要只按“成功路径”写。

## 🎓 这一关的知识点清单

| 知识点 | 说明 |
|--------|------|
| `requests.get()` | 发送 GET 请求 |
| `params={...}` | 查询参数 |
| `requests.post(..., data=...)` | 发送表单 |
| `requests.post(..., json=...)` | 发送 JSON |
| `response.status_code` | HTTP 状态码 |
| `response.headers` | 响应头 |
| `response.json()` | 解析 JSON 响应 |
| `timeout=3` | 设置请求超时 |
| `requests.Session()` | 保持 Cookie 和连接复用 |
| `raise_for_status()` | 让 HTTP 错误变成异常 |

## ➡️ 下一关

下一关：[TCP 编程](../58-tcp-programming/README.md)。

