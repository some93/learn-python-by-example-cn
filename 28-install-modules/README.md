# 第 28 关：安装第三方模块（师兄带你学 Python）

## 🎯 这一关你会学到

- 什么是 PyPI、pip 和第三方模块
- 为什么推荐用 `python -m pip` 而不是直接裸写 `pip`
- 如何用 `venv` 给项目创建独立虚拟环境
- `requirements.txt` 如何记录和安装依赖
- 安装依赖时常见的版本、环境、权限问题

## 🤔 先想一个问题

Python 标准库像手机出厂自带的应用：日历、相机、短信，够你完成很多基础任务。

第三方模块像应用商店里的 App：要发 HTTP 请求，可以装 `requests`；要做漂亮命令行输出，可以装 `rich`；要做数据分析，可以装 `pandas`。

但别把所有 App 都装进系统手机里。每个项目最好有自己的虚拟环境，就像每个项目一台独立手机，互不污染。

## 📖 看代码

```python
# 安装第三方模块
#
# 这一关的命令需要在终端里执行，例如：
# python -m pip install requests
#
# 为了保证示例代码离线也能运行，这里用内置 json 模块演示
# “导入模块 -> 调用模块功能 -> 得到结果” 的流程。

import json


print("=== 使用内置模块 json ===")

profile = {
    "name": "Alice",
    "age": 25,
    "skills": ["Python", "Web"],
}

json_text = json.dumps(profile, ensure_ascii=False, indent=2)
print(json_text)

parsed = json.loads(json_text)
print(parsed["name"])
print(parsed["skills"][0])
print(type(parsed).__name__)


print("\n=== requirements.txt 示例 ===")

requirements = [
    "requests==2.32.3",
    "rich==13.7.1",
]

print("\n".join(requirements))
```

## 🔍 师兄给你逐行拆

### 第三方模块装在哪里？

```bash
python -m pip install requests
```

**这行在干嘛？**

这条命令会用当前 Python 解释器对应的 pip，从 PyPI 下载并安装 `requests`。

**为什么推荐 `python -m pip`？**

很多电脑上可能同时有多个 Python：系统 Python、Anaconda、项目虚拟环境、Python 3.10、Python 3.12。

直接写：

```bash
pip install requests
```

你不一定知道它对应的是哪个 Python。

写成：

```bash
python -m pip install requests
```

意思更明确：用这个 `python` 对应的 pip 安装包。

---

### 虚拟环境：每个项目一套依赖

```bash
python -m venv .venv
```

**这行在干嘛？**

在当前项目目录创建一个 `.venv` 文件夹，里面有独立的 Python 解释器和第三方包目录。

激活虚拟环境：

```bash
# Windows PowerShell
.venv\Scripts\Activate.ps1

# macOS / Linux
source .venv/bin/activate
```

退出虚拟环境：

```bash
deactivate
```

**为什么要用虚拟环境？**

项目 A 需要 `requests==2.31`，项目 B 需要 `requests==2.32`。如果都装到全局环境，很容易互相打架。

虚拟环境就像给每个项目分配独立宿舍，谁也别把袜子扔到别人床上。

---

### 安装、查看、卸载模块

```bash
python -m pip install requests
python -m pip list
python -m pip show requests
python -m pip uninstall requests
```

**这几行在干嘛？**

- `install`：安装包；
- `list`：列出当前环境安装了哪些包；
- `show`：查看某个包的版本、位置、依赖；
- `uninstall`：卸载包。

**容易踩的坑**

安装失败时先确认三件事：

- 当前虚拟环境有没有激活；
- `python -m pip --version` 显示的路径是不是当前项目的 `.venv`；
- 包名有没有拼错。

---

### `requirements.txt` 记录依赖

```text
requests==2.32.3
rich==13.7.1
```

**这是什么？**

`requirements.txt` 是一份依赖清单。别人拿到你的项目后，只需要执行：

```bash
python -m pip install -r requirements.txt
```

就能安装同一批依赖。

**为什么要写版本号？**

如果只写：

```text
requests
```

下个月安装时可能拿到更新版本，行为可能变。写成 `requests==2.32.3`，可复现性更强。

---

### `pip freeze` 能导出依赖，但别盲信

```bash
python -m pip freeze > requirements.txt
```

**这行在干嘛？**

把当前环境里的所有包和版本导出到 `requirements.txt`。

**容易踩的坑**

如果你的环境很脏，里面装了一堆和项目无关的包，`pip freeze` 会一起导出来。更好的习惯是：

1. 先创建干净虚拟环境；
2. 只安装项目真正需要的包；
3. 再导出依赖。

---

### 示例代码为什么用 `json`？

```python
import json
```

**这行在干嘛？**

`json` 是 Python 标准库，不需要安装。这里用它演示模块的使用流程：导入模块、调用函数、处理返回值。

教程示例应该尽量离线可运行。如果示例直接 `import requests`，但你还没联网安装，程序就会报错。安装第三方模块的命令放在 README 里讲，代码文件保持稳定运行。

## 🏃 跑一下试试

```bash
$ python install-modules.py
=== 使用内置模块 json ===
{
  "name": "Alice",
  "age": 25,
  "skills": [
    "Python",
    "Web"
  ]
}
Alice
Python
dict

=== requirements.txt 示例 ===
requests==2.32.3
rich==13.7.1
```

## 💡 师兄的碎碎念

- 推荐用 `python -m pip ...`，避免 pip 和 Python 解释器对不上。
- 每个项目都建一个 `.venv`，不要把依赖全装进全局 Python。
- `requirements.txt` 记录依赖，`python -m pip install -r requirements.txt` 安装依赖。
- 版本号写得越明确，项目越容易复现。
- 教程代码尽量不要依赖网络和第三方包是否已安装，命令说明和可运行代码要分开。

## 🎓 这一关的知识点清单

- **PyPI**：Python 第三方包仓库。
- **pip**：Python 包安装工具，推荐通过 `python -m pip` 调用。
- **venv**：Python 标准库提供的虚拟环境工具。
- **requirements.txt**：记录项目依赖和版本的文本文件。
- **install/list/show/uninstall**：pip 的常用子命令。
- **可复现环境**：用虚拟环境和固定版本降低“我这里能跑你那里不能跑”的概率。

## ➡️ 下一关

模块和依赖搞定后，我们进入面向对象编程。下一关看类和实例：如何把数据和行为打包成对象 👉 [下一关：类和实例 →](../29-classes-and-instances/)


