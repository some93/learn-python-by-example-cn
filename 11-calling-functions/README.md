# 第 11 关：调用函数（师兄带你学 Python）

## 🎯 这一关你会学到

- Python 常用内置函数：`abs()`、`max()`、`min()`、`len()`、`sorted()`
- 类型转换函数：`int()`、`float()`、`str()`、`bool()`
- `isinstance()` 判断类型
- 参数传错时的报错信息怎么看

## 🤔 先想一个问题

Python 自带了一个「工具箱」，里面装着几十个常用函数，拿来就能用，不需要 `import`。就像奶茶店里的标准设备——制冰机、封杯机、搅拌机——你不需要自己造，直接用就行。这一关我们先学怎么**用**别人写好的函数，下一关再学怎么**写**自己的函数。

## 📖 看代码

```python
# 绝对值
print(abs(-10))       # 10

# 最大值 / 最小值
print(max(1, 2, 3))   # 3
print(min(-1, 0, 1))  # -1

# 类型转换
print(int('123'))      # 123
print(int(12.9))       # 12（截断不是四舍五入）
print(float('12.5'))   # 12.5
print(str(123))        # '123'
print(bool(''))        # False
print(bool(0))         # False

# hex()：转十六进制
print(hex(255))        # '0xff'

# sorted()：排序（返回新列表）
print(sorted([3, 1, 4, 1, 5]))  # [1, 1, 3, 4, 5]

# isinstance()：判断类型
print(isinstance(123, int))      # True
print(isinstance(123, (int, float)))  # True
```

## 🔍 师兄给你逐行拆

### 类型转换函数 —— 数据类型之间的翻译官

```python
print(int('123'))    # 字符串→整数
print(int(12.9))     # 浮点数→整数（直接截断小数部分）
```

**容易踩的坑**

`int()` 转浮点数是**截断**不是四舍五入！`int(12.9)` 是 `12`，`int(-12.9)` 是 `-12`。想四舍五入用 `round()`。另外，`int('12.5')` 会报错——不能直接把带小数点的字符串转 int，得先 `float()` 再 `int()`。

---

### `sorted()` vs `sort()` —— 别搞混

`sorted(list)` 返回一个**新列表**，原列表不变。`list.sort()` 是**原地排序**，返回 `None`。新手写 `new = lst.sort()` 然后困惑 `new` 为什么是 `None`，这是超高频错误。

## 🏃 跑一下试试

```bash
$ python calling-functions.py
10
3.14
3
-1
8
123
12
12.5
123
True
False
False
0xff
0x3e8
5
3
[1, 1, 3, 4, 5]
[4, 3, 1]
True
True
True
True
```

## 💡 师兄的碎碎念

- `help(abs)` 可以查看任何函数的文档，交互模式下特别好用。
- Python 内置函数完整列表可以查 `dir(__builtins__)`，有 60 多个。
- `round()` 的四舍五入遵循「银行家舍入法」（四舍六入五看奇偶），`round(0.5)` 是 `0` 不是 `1`！
- 函数名本身就是一个变量，可以赋值给其他变量：`my_abs = abs` 之后 `my_abs(-10)` 也返回 `10`。

## 🎓 这一关的知识点清单

- **数学函数**：`abs()` 绝对值、`max()`/`min()` 最大最小、`round()` 四舍五入。
- **类型转换**：`int()`、`float()`、`str()`、`bool()`，类型不兼容会报 `ValueError` 或 `TypeError`。
- **hex()**：整数转十六进制字符串。
- **sorted()**：排序，返回新列表。`reverse=True` 降序。
- **isinstance()**：判断对象是否是某类型，支持传入类型元组判断多种类型。

## ➡️ 下一关

会调用函数了，接下来学怎么**定义自己的函数** 👉 [下一关：定义函数 →](../12-defining-functions/)
