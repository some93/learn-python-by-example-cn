# 第 61 关：WSGI接口（师兄带你学 Python）

## 🎯 这一关你会学到

- 理解 WSGI 是什么
- 编写一个最简单的 WSGI 应用
- 了解 Web 服务器和应用的关系

## 🤔 先想一个问题

Web 服务器（Nginx）负责接收 HTTP 请求，Python 应用负责处理业务逻辑。它们之间怎么沟通？**WSGI** 就是这个「翻译官」——Python Web 应用的标准接口。

带着这个问题，我们来看代码。

## 📖 看代码

```python
# WSGI 接口

# WSGI = Web Server Gateway Interface
# 它是 Python Web 应用和 Web 服务器之间的标准接口

# 一个最简单的 WSGI 应用
def simple_app(environ, start_response):
    # environ：包含所有 HTTP 请求信息的字典
    # start_response：发送 HTTP 响应头的函数
    start_response('200 OK', [('Content-Type', 'text/html; charset=utf-8')])
    path = environ.get('PATH_INFO', '/')
    if path == '/':
        body = '<h1>首页</h1><p>这是一个 WSGI 应用！</p>'
    elif path == '/hello':
        body = '<h1>Hello!</h1><p>你好，世界！</p>'
    else:
        start_response('404 Not Found', [('Content-Type', 'text/html; charset=utf-8')])
        body = '<h1>404</h1><p>页面不存在</p>'
    return [body.encode('utf-8')]

# 用 Python 内置的 wsgiref 启动
if __name__ == '__main__':
    from wsgiref.simple_server import make_server

    print("启动 WSGI 服务器: http://127.0.0.1:8000")
    print("按 Ctrl+C 停止")

    server = make_server('127.0.0.1', 8000, simple_app)

    try:
        server.handle_request()    # 只处理一个请求（演示用）
        print("已处理一个请求，退出")
    except KeyboardInterrupt:
        print("\n服务器已停止")

# WSGI 的核心思想：
# 1. Web 服务器（如 Nginx）负责接收 HTTP 请求
# 2. WSGI 负责把请求转给 Python 应用
# 3. Python 应用处理请求，返回响应
# 4. 开发时用 wsgiref，生产环境用 Gunicorn、uWSGI 等
```

## 🔍 师兄给你逐行拆

> 代码已经在注释中做了详细说明，这里挑重点讲。

### 核心要点

- WSGI 应用就是一个函数：接收 `environ` 和 `start_response` 两个参数
- `environ` 是一个字典，包含所有 HTTP 请求信息
- `start_response` 用来发送 HTTP 响应头
- 开发用 `wsgiref.simple_server`，生产用 Gunicorn/uWSGI
- Flask/Django 底层都是 WSGI 应用

## 🏃 跑一下试试

```bash
cd 61-wsgi
python wsgi.py
```

## 💡 师兄的碎碎念

- WSGI 应用就是一个函数：接收 `environ` 和 `start_response` 两个参数
- `environ` 是一个字典，包含所有 HTTP 请求信息
- `start_response` 用来发送 HTTP 响应头
- 开发用 `wsgiref.simple_server`，生产用 Gunicorn/uWSGI
- Flask/Django 底层都是 WSGI 应用

## 🎓 这一关的知识点清单

| 知识点 | 说明 |
|--------|------|
| `def app(environ, start_response)` | WSGI 应用接口 |
| `environ` | 包含请求信息的字典 |
| `start_response(status, headers)` | 发送响应头 |
| `wsgiref.simple_server` | Python 内置的 WSGI 服务器 |

## ➡️ 下一关

下一关我们学习 [使用Web框架](../62-web-framework/README.md)，继续加油！
