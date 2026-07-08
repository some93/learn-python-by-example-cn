# 安装第三方模块
#
# 这一关真正要执行的安装命令在 README 里。
# 这个脚本不联网、不安装包，只把依赖管理流程打印出来，方便你先理解顺序。


print("=== 第三方模块从哪里来 ===")

# PyPI 是 Python 第三方包仓库，pip 是下载和安装这些包的工具。
package = "requests"
print(f"想使用第三方模块 {package!r}")
print("先确认当前项目使用哪个 Python，再用它调用 pip")


print("\n=== 推荐的项目依赖管理流程 ===")

steps = [
    "1. 创建虚拟环境: python -m venv .venv",
    "2. 激活虚拟环境: .venv\\Scripts\\Activate.ps1",
    "3. 安装第三方包: python -m pip install requests",
    "4. 在代码里导入: import requests",
    "5. 记录依赖版本: python -m pip freeze > requirements.txt",
    "6. 其他人安装依赖: python -m pip install -r requirements.txt",
]

for step in steps:
    print(step)


print("\n=== requirements.txt 示例 ===")

# requirements.txt 是给项目记录依赖的清单，不是 Python 代码。
requirements = [
    "requests==2.32.3",
    "rich==13.7.1",
]

print("\n".join(requirements))


print("\n=== 命令和代码的关系 ===")

# 安装发生在终端；import 发生在 Python 代码里。
examples = {
    "终端安装": "python -m pip install requests",
    "代码导入": "import requests",
    "终端导出": "python -m pip freeze > requirements.txt",
}

for action, command in examples.items():
    print(f"{action}: {command}")
