# 第 28 关：安装第三方模块

## 🎯 这一关你会学到

- 标准库、第三方模块、自己写的模块有什么区别
- PyPI、pip、venv、requirements.txt 分别负责什么
- 为什么推荐用 `python -m pip`，而不是直接写 `pip`
- 一个项目从创建虚拟环境到记录依赖的完整流程
- 为什么教程代码不直接联网安装第三方包

## 🤔 先想一个问题

上一关我们学了模块：一个 `.py` 文件可以被 `import`，标准库里的 `math`、`sys` 也可以被 `import`。

但现实项目里，你还会用别人写好的模块，比如：

- `requests`：发送 HTTP 请求；
- `rich`：做漂亮的命令行输出；
- `pandas`：处理表格数据；
- `flask`：写 Web 服务。

这些模块不是 Python 自带的，不能直接 `import`。你要先把它们安装到当前项目环境里。

这一关讲的不是某一个包怎么用，而是这条链路：

```text
PyPI 上有包 -> pip 下载安装到虚拟环境 -> 代码里 import -> requirements.txt 记录依赖
```

## 📖 看代码

```python
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
```

## 🔍 师兄给你拆开讲

### 先分清三类模块

**自己写的模块**：项目里的 `.py` 文件，比如上一关的 `modules.py`。

**标准库模块**：Python 自带的模块，比如 `math`、`json`、`datetime`、`sqlite3`。不用安装，直接 `import`。

**第三方模块**：别人发布到 PyPI 的模块，比如 `requests`、`flask`、`rich`。使用前要先安装。

所以顺序是：

```text
先安装 requests -> 再在代码里 import requests
```

不是反过来。

### PyPI 和 pip 是什么关系？

PyPI 可以理解成 Python 的应用商店。pip 是安装工具。

你在终端执行：

```bash
python -m pip install requests
```

意思是：用当前这个 `python` 对应的 pip，到 PyPI 下载并安装 `requests`。

### 为什么写 `python -m pip`？

很多电脑上可能同时有多个 Python：系统 Python、Anaconda、项目虚拟环境、Python 3.10、Python 3.12。

直接写：

```bash
pip install requests
```

你不一定知道这个 `pip` 属于哪个 Python。

写成：

```bash
python -m pip install requests
```

更明确：用当前这个 `python` 来运行 pip，包会装到当前 Python 对应的环境里。

### 为什么要虚拟环境？

不要把所有第三方包都装进全局 Python。项目 A 可能需要 `requests==2.31`，项目 B 可能需要 `requests==2.32`，全局安装很容易互相影响。

更稳的流程是每个项目一个 `.venv`：

```bash
python -m venv .venv
```

Windows PowerShell 激活：

```bash
.venv\Scripts\Activate.ps1
```

macOS / Linux 激活：

```bash
source .venv/bin/activate
```

退出虚拟环境：

```bash
deactivate
```

激活后再安装：

```bash
python -m pip install requests
```

### requirements.txt 是干什么的？

你安装了哪些第三方包，别人不知道。`requirements.txt` 就是项目依赖清单。

示例：

```text
requests==2.32.3
rich==13.7.1
```

别人拿到你的项目后执行：

```bash
python -m pip install -r requirements.txt
```

就能安装同一批依赖。

### pip freeze 要谨慎用

常见命令：

```bash
python -m pip freeze > requirements.txt
```

它会把当前环境里的所有包导出。问题是：如果你的环境不干净，里面有很多和项目无关的包，也会一起写进去。

更好的习惯是：

1. 先创建干净虚拟环境；
2. 只安装项目真正需要的包；
3. 再导出或手写 `requirements.txt`。

### 为什么示例脚本不真的安装 requests？

安装第三方包需要网络，也会改变你的 Python 环境。教程示例应该尽量可重复、可离线运行。

所以这一章的 `.py` 文件只打印正确流程；真正会修改环境的命令放在 README 里，由你在自己的项目里按需执行。

## 🏃 跑一下试试

```bash
cd 28-install-modules
python install-modules.py
```

输出：

```text
=== 第三方模块从哪里来 ===
想使用第三方模块 'requests'
先确认当前项目使用哪个 Python，再用它调用 pip

=== 推荐的项目依赖管理流程 ===
1. 创建虚拟环境: python -m venv .venv
2. 激活虚拟环境: .venv\Scripts\Activate.ps1
3. 安装第三方包: python -m pip install requests
4. 在代码里导入: import requests
5. 记录依赖版本: python -m pip freeze > requirements.txt
6. 其他人安装依赖: python -m pip install -r requirements.txt

=== requirements.txt 示例 ===
requests==2.32.3
rich==13.7.1

=== 命令和代码的关系 ===
终端安装: python -m pip install requests
代码导入: import requests
终端导出: python -m pip freeze > requirements.txt
```

## 💡 师兄的提醒

安装第三方模块时，先问三个问题：

- 我现在用的是哪个 Python？
- 我有没有在项目虚拟环境里？
- 这个依赖要不要写进 `requirements.txt`？

把这三个问题养成习惯，后面很多“我这里能跑，你那里不能跑”的环境问题会少很多。

## 🎓 这一关的知识点清单

| 知识点 | 说明 |
|--------|------|
| 标准库 | Python 自带模块，不需要安装 |
| 第三方模块 | PyPI 上别人发布的包，使用前要安装 |
| PyPI | Python 第三方包仓库 |
| pip | Python 包安装工具 |
| `python -m pip` | 用当前 Python 对应的 pip |
| venv | 给项目创建独立虚拟环境 |
| `requirements.txt` | 项目依赖清单 |
| `pip install -r` | 按清单安装依赖 |
| `pip freeze` | 导出当前环境依赖 |

## ➡️ 下一关

模块和依赖搞清楚后，我们进入面向对象编程。下一关：[类和实例](../29-classes-and-instances/)。
