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
    for path in ["/", "/hello?name=Alice", "/missing"]:
        status, body = fetch(base_url + path)
        print(status, body)

    thread.join()
    server.server_close()
