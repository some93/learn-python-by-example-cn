# 第 57 关：requests（师兄带你学 Python）

## 🎯 这一关你会学到

- 用 `requests` 发送 GET/POST 请求
- 处理请求参数和请求头
- 解析 JSON 响应
- 使用 Session 保持会话

## 🤔 先想一个问题

你想用 Python 调用一个 API、爬取网页内容、或者自动登录某个网站。Python 内置的 `urllib` 太难用了，`requests` 库让 HTTP 请求变得像说人话一样简单。

带着这个问题，我们来看代码。

## 📖 看代码

```python
# requests 库（HTTP 请求）

# 注意：需要先安装 pip install requests
# 以下代码仅作示例，运行需要网络连接

try:
    import requests

    # GET 请求
    r = requests.get('https://httpbin.org/get')
    print(f"状态码: {r.status_code}")
    print(f"响应头: {r.headers['Content-Type']}")
    print(f"内容: {r.text[:200]}")

    # 带参数的 GET
    r = requests.get('https://httpbin.org/get', params={'key': 'value', 'name': 'test'})
    print(f"\nURL: {r.url}")
    print(f"JSON: {r.json()}")

    # POST 请求
    r = requests.post('https://httpbin.org/post', data={'name': 'Alice', 'age': 25})
    print(f"\nPOST 结果: {r.json()['form']}")

    # 发送 JSON
    r = requests.post('https://httpbin.org/post', json={'name': 'Bob'})
    print(f"JSON POST: {r.json()['json']}")

    # 设置请求头
    headers = {'User-Agent': 'MyApp/1.0'}
    r = requests.get('https://httpbin.org/headers', headers=headers)
    print(f"\n请求头: {r.json()['headers']['User-Agent']}")

    # 超时设置（秒）
    r = requests.get('https://httpbin.org/get', timeout=5)

    # Session：保持 Cookie
    s = requests.Session()
    s.get('https://httpbin.org/cookies/set/token/abc123')
    r = s.get('https://httpbin.org/cookies')
    print(f"\nCookies: {r.json()}")

except ImportError:
    print("请先安装 requests: pip install requests")
except Exception as e:
    print(f"请求失败（可能没有网络）: {e}")

# requests 常用方法：
# requests.get(url)     GET 请求
# requests.post(url)    POST 请求
# requests.put(url)     PUT 请求
# requests.delete(url)  DELETE 请求
# r.status_code         HTTP 状态码
# r.text                响应文本
# r.json()              解析 JSON 响应
# r.content             响应二进制内容
```

## 🔍 师兄给你逐行拆

> 代码已经在注释中做了详细说明，这里挑重点讲。

### 核心要点

- `requests.get(url, params=dict)` 发送带参数的 GET 请求
- `requests.post(url, json=dict)` 发送 JSON 数据
- `r.json()` 直接把响应解析为 Python 字典
- `timeout=5` 设置超时，避免请求卡住
- `Session` 对象自动管理 Cookie，适合需要登录的场景

## 🏃 跑一下试试

```bash
cd 57-requests
python requests_demo.py
```

## 💡 师兄的碎碎念

- `requests.get(url, params=dict)` 发送带参数的 GET 请求
- `requests.post(url, json=dict)` 发送 JSON 数据
- `r.json()` 直接把响应解析为 Python 字典
- `timeout=5` 设置超时，避免请求卡住
- `Session` 对象自动管理 Cookie，适合需要登录的场景

## 🎓 这一关的知识点清单

| 知识点 | 说明 |
|--------|------|
| `requests.get(url)` | 发送 GET 请求 |
| `requests.post(url, json=...)` | 发送 POST 请求 |
| `r.status_code` | HTTP 状态码 |
| `r.json()` | 解析 JSON 响应 |
| `r.text / r.content` | 获取文本/二进制响应 |
| `requests.Session()` | 保持会话的 Session |

## ➡️ 下一关

下一关我们学习 [TCP编程](../58-tcp-programming/README.md)，继续加油！
