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
