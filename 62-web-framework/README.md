# 第 62 关：使用Web框架（师兄带你学 Python）

## 🎯 这一关你会学到

- 了解 Web 框架的作用
- 用 Flask 定义路由
- 处理 GET/POST 请求
- 返回 JSON 响应

## 🤔 先想一个问题

直接写 WSGI 太底层了，你得自己解析 URL、处理参数、管理路由……Web 框架帮你把这些脏活全干了，你只需要写业务逻辑。

带着这个问题，我们来看代码。

## 📖 看代码

```python
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
```

## 🔍 师兄给你逐行拆

> 代码已经在注释中做了详细说明，这里挑重点讲。

### 核心要点

- Flask 用 `@app.route()` 装饰器定义路由，简洁直观
- `<name>` 语法可以从 URL 中提取变量
- `request.args` 获取 GET 参数，`request.get_json()` 获取 POST JSON
- `jsonify()` 返回 JSON 响应
- Flask 适合小项目和 API，Django 适合大型项目

## 🏃 跑一下试试

```bash
cd 62-web-framework
python web-framework.py
```

## 💡 师兄的碎碎念

- Flask 用 `@app.route()` 装饰器定义路由，简洁直观
- `<name>` 语法可以从 URL 中提取变量
- `request.args` 获取 GET 参数，`request.get_json()` 获取 POST JSON
- `jsonify()` 返回 JSON 响应
- Flask 适合小项目和 API，Django 适合大型项目

## 🎓 这一关的知识点清单

| 知识点 | 说明 |
|--------|------|
| `@app.route(path)` | 定义路由 |
| `@app.route(path, methods=['POST'])` | 指定请求方法 |
| `request.args.get(key)` | 获取 GET 参数 |
| `request.get_json()` | 获取 POST JSON 数据 |
| `jsonify(dict)` | 返回 JSON 响应 |
| `Flask vs Django` | 微框架 vs 全功能框架 |

## ➡️ 下一关

下一关我们学习 [异步IO](../63-async-io/README.md)，继续加油！
