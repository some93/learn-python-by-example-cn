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
    print(math.sqrt(16))  # 4.0

    # from math import pi 后，可以直接使用 pi。
    print(pi)  # 3.141592653589793


def show_scope_examples():
    print("\n=== 公开和约定私有 ===")
    print(public_func())  # 我是公开函数
    # 约定私有不是语法禁止，只是社区约定。
    print(_private_func())  # 我是约定私有函数
    print(PI)  # 3.14159
    print(_INTERNAL_VERSION)  # 1.0


def main():
    print("=== __name__ 和命令行参数 ===")
    # 直接运行本文件时，__name__ 的值是 "__main__"。
    print(__name__)  # __main__

    # sys.argv[0] 是脚本名，所以这里从第 1 个参数开始取。
    args = sys.argv[1:]
    if args:
        print(f"参数: {args}")  # 参数: ['hello', '123']
    else:
        print("没有额外参数")  # 没有额外参数

    show_import_examples()
    show_scope_examples()


if __name__ == "__main__":
    # 只有直接运行本文件时才执行 main()；被 import 时不会执行。
    main()
