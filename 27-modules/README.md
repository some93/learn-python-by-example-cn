# 第 27 关：模块（师兄带你学 Python）

## 🎯 这一关你会学到

- Python 模块系统
- import 的多种方式
- __name__ == '__main__' 的含义
- 作用域：公开 vs 私有

## 🤔 先想一个问题

模块像乐高积木的零件包——每包有特定功能。你 import 需要的包，拼出想要的东西，不用从头造轮子。

## 📖 看代码

```python
# 模块（Module）

# Python 用模块组织代码，一个 .py 文件就是一个模块

# 标准模块结构
"""
这是模块的文档字符串（docstring）
"""

import sys

def test():
    # sys.argv 包含命令行参数
    args = sys.argv
    if len(args) == 1:
        print("没有额外参数")
    else:
        print(f"参数: {args[1:]}")

# __name__ 变量
# 当模块被直接运行时，__name__ 是 '__main__'
# 当模块被 import 时，__name__ 是模块名
if __name__ == '__main__':
    test()

# 作用域
# _xxx：约定私有（不建议外部访问）
# __xxx：强制私有（名字改编）
# xxx：公开

def _private_func():
    return "我是私有函数"

def public_func():
    return "我是公开函数"

PI = 3.14159   # 公开常量
_INTERNAL = 42  # 私有常量

# import 的几种方式
# import math              # 导入整个模块
# from math import sqrt    # 只导入 sqrt
# from math import *       # 导入所有（不推荐！）
# import math as m         # 起别名

import math
print(math.sqrt(16))       # 4.0

from math import pi
print(pi)                   # 3.141592653589793
```

## 🔍 师兄给你逐行拆

Python 用模块组织代码——一个 .py 文件就是一个模块。通过 import 可以使用其他模块的功能。

代码中的关键点已经在注释中标注，结合上面的完整代码逐段阅读即可。更多细节请运行代码观察输出。

## 🏃 跑一下试试

```bash
$ python modules.py
```

运行代码，观察输出，对照注释理解每一行。

## 💡 师兄的碎碎念

- **import module / from module import func**
- **__name__ == '__main__' 入口判断**
- **_xxx 约定私有 / __xxx 强制私有**
- **包(package) = 目录 + __init__.py**

## 🎓 这一关的知识点清单

- **Python 模块系统**
- **import 的多种方式**
- **__name__ == '__main__' 的含义**
- **作用域：公开 vs 私有**

## ➡️ 下一关

本关搞定！接下来学 安装第三方模块 👉 [下一关：安装第三方模块 →](../28-install-modules/)
