# 第 61 关：WSGI 接口（师兄带你学 Python）

## 🎯 这一关你会学到

- WSGI 是什么，解决 Web 服务器和 Python 应用之间的什么问题
- 一个 WSGI 应用函数的标准签名
- `environ` 里有什么
- `start_response(status, headers)` 什么时候调用
- WSGI 应用为什么返回 `bytes` 可迭代对象
- `wsgiref.simple_server` 如何在本地演示 WSGI

## 🤔 先想一个问题

浏览器发来 HTTP 请求，Python 代码要返回 HTTP 响应。中间需要一个约定：服务器怎么把请求交给 Python？Python 又怎么把状态码、响应头、响应体交回服务器？

WSGI 就是这个约定。它不是框架，而是接口标准。Flask、Django 这类同步 Web 框架，底层都能作为 WSGI 应用运行。

## 📖 看代码

```python
# WSGI 接口

from urllib.parse import parse_qs
from urllib.request import Request, urlopen
from wsgiref.simple_server import WSGIRequestHandler, make_server
import threading


def application(environ, start_response):
    # environ 是 WSGI 服务器整理好的请求信息字典。
    path = environ.get("PATH_INFO", "/")
    query = parse_qs(environ.get("QUERY_STRING", ""))

    if path == "/":
        status = "200 OK"
        body = "首页"
    elif path == "/hello":
        status = "200 OK"
        name = query.get("name", ["World"])[0]
        body = f"Hello, {name}"
    else:
        status = "404 Not Found"
        body = "页面不存在"

    response_body = body.encode("utf-8")
    headers = [
        ("Content-Type", "text/plain; charset=utf-8"),
        ("Content-Length", str(len(response_body))),
    ]

    # start_response 只能在确定状态码和响应头后调用。
    start_response(status, headers)
    return [response_body]


class QuietHandler(WSGIRequestHandler):
    def log_message(self, format, *args):
        # 关闭默认访问日志，让教程输出只保留我们关心的内容。
        return


def run_server(server, request_count):
    for _ in range(request_count):
        server.handle_request()


def fetch(url):
    try:
        with urlopen(Request(url), timeout=3) as response:
            return response.status, response.read().decode("utf-8")
    except Exception as error:
        # urllib 遇到 404 会抛 HTTPError，它也有 status 和 read()。
        if hasattr(error, "status"):
            return error.status, error.read().decode("utf-8")
        raise


if __name__ == "__main__":
    # 端口传 0，避免固定端口和本机其他服务冲突。
    server = make_server("127.0.0.1", 0, application, handler_class=QuietHandler)
    base_url = f"http://127.0.0.1:{server.server_port}"

    thread = threading.Thread(target=run_server, args=(server, 3))
    thread.start()

    print("=== WSGI 应用响应 ===")
    for path in ["/", "/hello?name=Alice", "/missing"]:   # 依次输出：200 首页 / 200 Hello, Alice / 404 页面不存在
        status, body = fetch(base_url + path)
        print(status, body)

    thread.join()
    server.server_close()
```

## 🔍 师兄给你拆开讲

WSGI 应用就是一个可调用对象，最常见是函数：

```python
def application(environ, start_response):
    ...
```

`environ` 是字典，里面有请求方法、路径、查询字符串、请求头等信息。示例用到了 `PATH_INFO` 和 `QUERY_STRING`。

`start_response(status, headers)` 用来告诉服务器状态码和响应头。要先确定是 `200 OK` 还是 `404 Not Found`，再调用它。不要像初学示例里常见的那样先发 200，发现错误后又发 404。

返回值必须是一个可迭代对象，里面是 `bytes`。所以字符串响应要先 `.encode("utf-8")`。

`wsgiref.simple_server` 是标准库里的演示服务器，适合学习和测试 WSGI 接口。生产环境通常用 Gunicorn、uWSGI 等 WSGI 服务器，再由 Nginx 做反向代理。

## 🏃 跑一下试试

```bash
cd 61-wsgi
python wsgi.py
```

输出：

```text
=== WSGI 应用响应 ===
200 首页
200 Hello, Alice
404 页面不存在
```

## 💡 师兄的提醒

WSGI 的价值在于解耦：服务器负责监听端口、解析 HTTP、管理连接；应用负责业务逻辑和返回响应。

你平时写 Flask/Django 不会直接接触太多 WSGI，但理解它能帮你搞清楚“框架、应用服务器、Nginx”之间的关系。

## 🎓 这一关的知识点清单

| 知识点 | 说明 |
|--------|------|
| WSGI | Python Web 服务器和应用之间的同步接口 |
| `application(environ, start_response)` | WSGI 应用函数签名 |
| `environ` | 请求信息字典 |
| `PATH_INFO` | 请求路径 |
| `QUERY_STRING` | 查询字符串 |
| `start_response()` | 发送状态码和响应头 |
| 返回 `bytes` 可迭代对象 | WSGI 响应体格式 |
| `wsgiref.simple_server` | 标准库演示 WSGI 服务器 |

## ➡️ 下一关

下一关：[使用 Web 框架](../62-web-framework/README.md)。
