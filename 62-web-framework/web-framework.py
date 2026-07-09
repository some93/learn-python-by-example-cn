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
