# 第 27 关：模块（师兄带你学 Python）

## 🎯 这一关你会学到

- 一个 `.py` 文件就是一个模块
- `import`、`from ... import ...`、`as` 的区别
- `__name__ == "__main__"` 的真实用途
- 模块里的公开名字和约定私有名字
- 为什么入口代码通常放在文件底部

## 🤔 先想一个问题

模块像乐高零件包。你写程序不可能每次都从泥土开始烧砖，标准库和第三方库已经给你准备了大量零件。

`import` 就是把需要的零件包拿过来。拿整个包、只拿某个零件、给零件包起个短名字，都可以。

## 📖 看代码

```python
"""演示 Python 模块的基本写法。"""

import math
import sys
from math import pi

# 全大写变量通常表示常量，但 Python 不会强制禁止修改。
PI = 3.14159

# 单下划线开头表示“约定私有”，提醒外部代码不要直接使用。
_INTERNAL_VERSION = "1.0"


def public_func():
    return "我是公开函数"


def _private_func():
    return "我是约定私有函数"


def show_import_examples():
    print("=== import 的几种常见写法 ===")
    # import math 后，需要通过模块名访问函数。
    print(math.sqrt(16))

    # from math import pi 后，可以直接使用 pi。
    print(pi)


def show_scope_examples():
    print("\n=== 公开和约定私有 ===")
    print(public_func())
    # 约定私有不是语法禁止，只是社区约定。
    print(_private_func())
    print(PI)
    print(_INTERNAL_VERSION)


def main():
    print("=== __name__ 和命令行参数 ===")
    # 直接运行本文件时，__name__ 的值是 "__main__"。
    print(__name__)

    # sys.argv[0] 是脚本名，所以这里从第 1 个参数开始取。
    args = sys.argv[1:]
    if args:
        print(f"参数: {args}")
    else:
        print("没有额外参数")

    show_import_examples()
    show_scope_examples()


if __name__ == "__main__":
    # 只有直接运行本文件时才执行 main()；被 import 时不会执行。
    main()
```

## 🔍 师兄给你逐行拆

### 模块文档字符串

```python
"""演示 Python 模块的基本写法。"""
```

**这行在干嘛？**

文件开头的字符串叫模块文档字符串，也就是 module docstring。它用来说明这个模块是干什么的。

**为什么这么写？**

别人用 `help(modules)` 或文档工具读取模块时，可以看到这段说明。小脚本可以不写，但正式模块建议写一句。

---

### `import math` 和 `from math import pi`

```python
import math
import sys
from math import pi
```

**这行在干嘛？**

`import math` 是导入整个 `math` 模块，使用时要写：

```python
math.sqrt(16)
```

`from math import pi` 是只把 `math` 模块里的 `pi` 这个名字导入当前模块，使用时可以直接写：

```python
pi
```

**怎么选？**

一般优先 `import module`，命名空间更清楚。比如 `math.sqrt()` 一看就知道来自 `math`。

`from module import name` 适合导入少量非常明确的名字。

**容易踩的坑**

尽量别写：

```python
from math import *
```

它会把很多名字一股脑塞进当前文件，容易覆盖你自己定义的变量，也让读代码的人不知道某个名字从哪来。

---

### 公开名字和约定私有名字

```python
PI = 3.14159
_INTERNAL_VERSION = "1.0"


def public_func():
    return "我是公开函数"


def _private_func():
    return "我是约定私有函数"
```

**这行在干嘛？**

不以下划线开头的名字，比如 `PI`、`public_func`，通常表示给外部使用。

以下划线开头的名字，比如 `_INTERNAL_VERSION`、`_private_func`，表示内部使用，不建议外部直接访问。

**为什么说是“约定私有”？**

Python 不会真的禁止你访问 `_private_func()`。下划线更像一个提示牌：这是内部实现，外部别依赖它，后续可能改。

---

### `sys.argv` —— 读取命令行参数

```python
args = sys.argv[1:]
if args:
    print(f"参数: {args}")
else:
    print("没有额外参数")
```

**这行在干嘛？**

`sys.argv` 是一个列表，保存命令行参数。

如果你运行：

```bash
python modules.py hello 123
```

那么：

```python
sys.argv[0]  # 脚本路径
sys.argv[1:] # ['hello', '123']
```

所以我们通常用 `sys.argv[1:]` 获取真正传给程序的参数。

---

### `__name__ == "__main__"` —— 入口保护

```python
if __name__ == "__main__":
    main()
```

**这行在干嘛？**

当这个文件被直接运行时，`__name__` 的值是 `"__main__"`，于是会执行 `main()`。

当这个文件被别的文件 `import` 时，`__name__` 的值是模块名，比如 `"modules"`，这段入口代码就不会执行。

**为什么重要？**

一个 `.py` 文件经常有两种身份：

- 直接运行：当脚本用；
- 被导入：当模块用。

入口保护能避免“别人只是 import 你，结果你立刻跑了一堆演示代码”的尴尬。

**为什么入口代码放底部？**

因为前面要先定义好常量和函数，最后再决定是否调用 `main()`。这是 Python 脚本的常见结构。

## 🏃 跑一下试试

```bash
$ python modules.py
=== __name__ 和命令行参数 ===
__main__
没有额外参数
=== import 的几种常见写法 ===
4.0
3.141592653589793

=== 公开和约定私有 ===
我是公开函数
我是约定私有函数
3.14159
1.0
```

带参数运行：

```bash
$ python modules.py hello 123
=== __name__ 和命令行参数 ===
__main__
参数: ['hello', '123']
=== import 的几种常见写法 ===
4.0
3.141592653589793

=== 公开和约定私有 ===
我是公开函数
我是约定私有函数
3.14159
1.0
```

## 💡 师兄的碎碎念

- 一个 `.py` 文件就是一个模块，文件名就是模块名。
- `import math` 导入模块，使用时写 `math.sqrt()`；`from math import pi` 只导入某个名字。
- `from module import *` 新手尽量别用，命名来源会变乱。
- `_name` 是约定私有，不是强制私有。
- 可执行脚本建议把入口逻辑放进 `main()`，最后用 `if __name__ == "__main__": main()` 调用。

## 🎓 这一关的知识点清单

- **模块**：一个 `.py` 文件就是一个模块，用来组织代码。
- **import**：导入模块或模块里的名字，复用已有功能。
- **sys.argv**：读取命令行参数，`sys.argv[1:]` 是用户传入的参数。
- **__name__**：模块的特殊变量，直接运行时是 `"__main__"`，被导入时是模块名。
- **入口保护**：`if __name__ == "__main__":` 防止 import 时自动执行脚本逻辑。
- **约定私有**：以下划线开头的名字表示内部使用。

## ➡️ 下一关

模块讲完，就该学怎么安装别人写好的模块了。下一关看 `pip`、虚拟环境和 `requirements.txt` 👉 [下一关：安装第三方模块 →](../28-install-modules/)


