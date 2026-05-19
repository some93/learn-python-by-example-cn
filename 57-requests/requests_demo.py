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
