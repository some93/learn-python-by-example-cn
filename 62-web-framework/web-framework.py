# 使用 Web 框架（Flask）

# 注意：需要安装 pip install flask
# 以下代码展示 Flask 的基本用法

try:
    from flask import Flask, request, jsonify

    app = Flask(__name__)

    # 路由：URL 映射到函数
    @app.route('/')
    def index():
        return '<h1>首页</h1><p>欢迎使用 Flask！</p>'

    @app.route('/hello/<name>')
    def hello(name):
        return f'<h1>Hello, {name}!</h1>'

    # 获取请求参数
    @app.route('/greet')
    def greet():
        name = request.args.get('name', 'World')
        return f'<h1>Hello, {name}!</h1>'

    # 处理 POST 请求
    @app.route('/api/user', methods=['POST'])
    def create_user():
        data = request.get_json()
        return jsonify({
            'status': 'ok',
            'user': data
        })

    # 错误处理
    @app.errorhandler(404)
    def not_found(e):
        return '<h1>404</h1><p>页面不存在</p>', 404

    if __name__ == '__main__':
        print("Flask 应用示例")
        print("路由列表：")
        print("  GET  /          -> 首页")
        print("  GET  /hello/<n> -> 问候")
        print("  GET  /greet     -> 带参数问候")
        print("  POST /api/user  -> 创建用户")
        # app.run(debug=True)  # 取消注释启动服务器

except ImportError:
    print("请先安装 Flask: pip install flask")
    print()
    print("Flask 是最流行的 Python Web 框架之一")
    print("特点：轻量、灵活、扩展性强")
    print("适合：小型项目、API 服务、快速原型")

# Flask vs Django：
# Flask：微框架，只提供核心功能，其他靠扩展
# Django：全功能框架，自带 ORM、Admin、认证等
# 选择建议：小项目用 Flask，大项目用 Django
