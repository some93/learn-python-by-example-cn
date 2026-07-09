# 第 62 关：使用 Web 框架（师兄带你学 Python）

## 🎯 这一关你会学到

- Web 框架在 WSGI 之上帮你解决什么问题
- 如何用 Flask 定义 GET / POST 路由
- 如何读取路径参数和查询参数
- 如何读取 JSON 请求体
- 如何返回 JSON 和状态码
- 如何写 404 错误处理
- 如何用 `test_client()` 离线测试接口

## 🤔 先想一个问题

上一关直接写 WSGI，你要自己判断路径、解析查询参数、组装状态码和响应头。真实项目这样写太累了。

Web 框架的价值是把常见 Web 工作抽象好：路由匹配、请求对象、响应对象、JSON、错误处理、中间件、测试工具。你把精力放在业务逻辑上。

Flask 是一个轻量 Web 框架。使用前需要安装：

```bash
python -m pip install flask
```

## 📖 看代码

```python
# 使用 Web 框架（Flask）

try:
    from flask import Flask, jsonify, request
except ImportError:
    Flask = None


def create_app():
    app = Flask(__name__)

    @app.get("/")
    def index():
        # 返回字符串时，Flask 会自动包装成 HTTP 响应。
        return "欢迎使用 Flask"

    @app.get("/hello/<name>")
    def hello(name):
        # URL 里的 <name> 会作为函数参数传进来。
        return f"Hello, {name}"

    @app.get("/greet")
    def greet():
        # request.args 用来读取查询参数。
        name = request.args.get("name", "World")
        return jsonify({"message": f"Hello, {name}"})

    @app.post("/api/users")
    def create_user():
        # silent=True 表示 JSON 无效时返回 None，而不是直接抛异常。
        data = request.get_json(silent=True) or {}
        name = data.get("name")

        if not name:
            return jsonify({"error": "name is required"}), 400

        return jsonify({"id": 1, "name": name}), 201

    @app.errorhandler(404)
    def not_found(error):
        # 错误处理函数也可以返回 JSON 和状态码。
        return jsonify({"error": "not found"}), 404

    return app


def main():
    if Flask is None:
        print("请先安装 Flask: python -m pip install flask")
        return

    app = create_app()

    # test_client 不需要真的启动端口，适合教程、测试和 CI。
    client = app.test_client()

    print("=== GET 路由 ===")
    response = client.get("/")
    print(response.status_code, response.get_data(as_text=True))  # 200 欢迎使用 Flask

    response = client.get("/hello/Alice")
    print(response.status_code, response.get_data(as_text=True))  # 200 Hello, Alice

    print("\n=== 查询参数和 JSON 响应 ===")
    response = client.get("/greet?name=Bob")
    print(response.status_code, response.get_json())  # 200 {'message': 'Hello, Bob'}

    print("\n=== POST JSON ===")
    response = client.post("/api/users", json={"name": "Charlie"})
    print(response.status_code, response.get_json())  # 201 {'id': 1, 'name': 'Charlie'}

    response = client.post("/api/users", json={})
    print(response.status_code, response.get_json())  # 400 {'error': 'name is required'}

    print("\n=== 404 错误处理 ===")
    response = client.get("/missing")
    print(response.status_code, response.get_json())  # 404 {'error': 'not found'}


if __name__ == "__main__":
    main()
```

## 🔍 师兄给你拆开讲

`create_app()` 是常见写法，叫应用工厂。测试、配置、多环境部署时，比在全局直接写死 `app = Flask(__name__)` 更灵活。

`@app.get("/")` 和 `@app.post("/api/users")` 是路由装饰器，把 URL 和函数绑定起来。浏览器或客户端请求这个路径时，Flask 调用对应函数。

`/hello/<name>` 里的 `<name>` 是路径参数，会传给 `hello(name)`。`request.args` 读取查询参数，比如 `/greet?name=Bob`。

`request.get_json()` 读取 JSON 请求体。示例里用 `silent=True`，表示请求体不是合法 JSON 时返回 `None`，方便我们自己返回 400。

`jsonify()` 返回 JSON 响应。函数可以返回 `(body, status_code)`，例如 `return jsonify(...), 201`。

`app.test_client()` 不需要真正启动服务器，能直接模拟 HTTP 请求。写接口测试时非常好用，也适合教程稳定演示。

## 🏃 跑一下试试

```bash
cd 62-web-framework
python web-framework.py
```

输出：

```text
=== GET 路由 ===
200 欢迎使用 Flask
200 Hello, Alice

=== 查询参数和 JSON 响应 ===
200 {'message': 'Hello, Bob'}

=== POST JSON ===
201 {'id': 1, 'name': 'Charlie'}
400 {'error': 'name is required'}

=== 404 错误处理 ===
404 {'error': 'not found'}
```

## 💡 师兄的提醒

Flask 是微框架，核心轻量，扩展自由；Django 是全功能框架，自带 ORM、Admin、认证等。小型 API、原型、脚本后台常用 Flask；复杂业务后台常会考虑 Django 或 FastAPI。

开发服务器只适合本地开发。生产环境要使用 Gunicorn、uWSGI、Uvicorn 等应用服务器，并放在 Nginx 等反向代理后面。

## 🎓 这一关的知识点清单

| 知识点 | 说明 |
|--------|------|
| `Flask(__name__)` | 创建 Flask 应用 |
| 应用工厂 | 用函数创建并配置 app |
| `@app.get()` / `@app.post()` | 定义路由和请求方法 |
| `<name>` | 路径参数 |
| `request.args` | 查询参数 |
| `request.get_json()` | JSON 请求体 |
| `jsonify()` | 返回 JSON 响应 |
| `(response, status)` | 同时返回响应体和状态码 |
| `@app.errorhandler(404)` | 自定义错误处理 |
| `app.test_client()` | 测试客户端 |

## ➡️ 下一关

下一关：[异步 IO](../63-async-io/README.md)。
