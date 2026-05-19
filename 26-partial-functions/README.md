# 第 26 关：偏函数（师兄带你学 Python）

## 🎯 这一关你会学到

- functools.partial
- 固定函数的某些参数
- 简化频繁调用的写法
- partial 的等价手动实现

## 🤔 先想一个问题

你每天去同一家奶茶店点「中杯、少糖、加珍珠」。partial 就是设置了一个「常用订单」按钮——以后点单只说「老样子」就行。

## 📖 看代码

```python
# 偏函数（Partial Function）

import functools

# int() 默认按十进制转换
print(int('12345'))        # 12345

# int() 可以指定进制
print(int('12345', base=8))    # 5349（八进制）
print(int('12345', base=16))   # 74565（十六进制）

# 如果经常需要转二进制，每次写 base=2 很麻烦
# 用 functools.partial 创建偏函数
int2 = functools.partial(int, base=2)

print(int2('1000000'))    # 64
print(int2('1010101'))    # 85

# partial 的本质：固定函数的某些参数
# int2('1010101') 等价于 int('1010101', base=2)

# 也可以固定位置参数
max10 = functools.partial(max, 10)
print(max10(5, 6, 7))    # 10（等价于 max(10, 5, 6, 7)）

# 自己实现 partial 的效果
def int16(s):
    return int(s, base=16)

print(int16('ff'))    # 255
```

## 🔍 师兄给你逐行拆

偏函数把一个函数的某些参数固定住，返回一个新的更简洁的函数。适合你经常用同样参数调用某个函数的场景。

代码中的关键点已经在注释中标注，结合上面的完整代码逐段阅读即可。更多细节请运行代码观察输出。

## 🏃 跑一下试试

```bash
$ python partial-functions.py
```

运行代码，观察输出，对照注释理解每一行。

## 💡 师兄的碎碎念

- **functools.partial(func, *args, **kwargs)**
- **int2 = partial(int, base=2)**
- **固定位置参数或关键字参数**
- **等价于手写一个包装函数**

## 🎓 这一关的知识点清单

- **functools.partial**
- **固定函数的某些参数**
- **简化频繁调用的写法**
- **partial 的等价手动实现**

## ➡️ 下一关

本关搞定！接下来学 模块 👉 [下一关：模块 →](../27-modules/)
