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
