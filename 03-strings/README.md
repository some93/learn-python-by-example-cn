# 第 3 关：字符串和编码

## 🎯 这一关你会学到

- 字符串的多种写法：转义、原始字符串、多行字符串
- 字符与编码的关系：ASCII、Unicode、UTF-8
- `ord()`/`chr()`、`encode()`/`decode()` 的用法
- 三种格式化字符串的方式（重点掌握 f-string）

## 🤔 先想一个问题

你发微信的时候，输入的是中文汉字，但手机底层传输的是 0 和 1 的二进制数据。**从你看到的「你好」到计算机传输的 `\xe4\xbd\xa0\xe5\xa5\xbd`，中间发生了什么？** 这就是编码问题——把人类看得懂的字符，翻译成机器看得懂的字节。搞懂这一关，你就再也不会被 `UnicodeDecodeError` 折磨了。

## 📖 看代码

```python
# 转义字符
print("hello\nworld")       # 输出两行：hello / world
print("hello\tworld")       # hello	world
print("hello\\world")       # hello\world

# r'' 原始字符串：不转义
print(r"hello\nworld")      # hello\nworld

# '''...''' 多行字符串
print('''第一行
第二行
第三行''')              # 输出三行：第一行 / 第二行 / 第三行

# ord() 和 chr()：字符与编码互转
print(ord('A'))     # 65
print(ord('中'))    # 20013
print(chr(65))      # A
print(chr(20013))   # 中

# encode() 和 decode()：字符串与字节互转
print('ABC'.encode('ascii'))       # b'ABC'
print('中文'.encode('utf-8'))       # b'\xe4\xb8\xad\xe6\x96\x87'
print(b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8'))  # 中文

# len() 对字符串和字节的区别
print(len('中文'))                   # 2（字符数）
print(len('中文'.encode('utf-8')))   # 6（字节数）

# 格式化：f-string（推荐！）
name = "Charlie"
age = 35
print(f"Hello, {name}. You are {age} years old.")  # Hello, Charlie. You are 35 years old.
print(f"计算结果: {1 + 2 + 3}")  # 计算结果: 6
print(f"保留两位小数: {3.14159:.2f}")  # 保留两位小数: 3.14
```

## 🔍 师兄给你逐行拆

### 转义字符 —— 看不见的「特殊指令」

```python
print("hello\nworld")    # 换行
print(r"hello\nworld")   # 原样输出
```

**这行在干嘛？**

`\n` 是换行符，`\t` 是制表符，`\\` 是反斜杠本身。这些以 `\` 开头的叫**转义字符**，告诉 Python「这不是普通字符，有特殊含义」。

如果你不想转义，在字符串前加 `r`（raw），所有 `\` 都被当作普通字符。写正则表达式和 Windows 文件路径时特别好用：`r"C:\Users\name"` 比 `"C:\\Users\\name"` 清爽多了。

---

### `ord()` 和 `chr()` —— 字符和数字之间的翻译官

```python
print(ord('A'))     # 65
print(chr(20013))   # 中
```

**这行在干嘛？**

`ord()` 把字符变成 Unicode 编码数字，`chr()` 反过来。Python 3 的字符串底层全是 **Unicode**，所以不管是英文 `A` 还是中文 `中`，都有一个唯一的编码数字。

---

### `encode()` 和 `decode()` —— 字符串和字节的桥梁

```python
print('中文'.encode('utf-8'))       # b'\xe4\xb8\xad\xe6\x96\x87'
print(b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8'))  # 中文
```

**这行在干嘛？**

`encode()` 把字符串（str）编码成字节（bytes），`decode()` 把字节解码回字符串。`b'...'` 前缀表示这是字节数据。

**生活类比**

字符串是你说的「中文」，字节是快递包裹里的二进制数据。`encode()` 是「打包发货」，`decode()` 是「拆包验收」。打包和拆包必须用**同一种编码方式**（UTF-8），否则拆出来就是乱码——就像用中文说明书去拆日语快递，肯定搞不明白。

**容易踩的坑**

中文不能用 `ascii` 编码（`'中文'.encode('ascii')` 会报 `UnicodeEncodeError`），因为 ASCII 只认英文字母。处理中文一律用 **UTF-8**。

---

### 格式化字符串 —— 三代人的进化

```python
# 第一代：% 操作符
print("Hello, %s" % "Alice")

# 第二代：format()
print("Hello, {}".format("Bob"))

# 第三代：f-string（推荐！）
name = "Charlie"
print(f"Hello, {name}")
```

**为什么推荐 f-string？**

1. **最简洁**：变量直接写在花括号里，不用额外传参
2. **支持表达式**：`f"{1+2}"` 直接算出 `3`
3. **支持格式化**：`f"{3.14:.1f}"` 保留一位小数
4. Python 3.6+ 才有，但现在已经是主流标准

## 🏃 跑一下试试

```bash
$ python strings.py
hello
world
hello	world
hello\world
hello\nworld
第一行
第二行
第三行
65
20013
A
中
b'ABC'
b'\xe4\xb8\xad\xe6\x96\x87'
中文
2
6
Hello, Charlie. You are 35 years old.
计算结果: 6
保留两位小数: 3.14
```

## 💡 师兄的碎碎念

- Python 3 的字符串默认就是 Unicode，彻底解决了 Python 2 时代的中文编码噩梦。如果你用的是 Python 3，恭喜你躲过了一劫。
- 源码文件开头加 `# -*- coding: utf-8 -*-` 是 Python 2 的遗留习惯，Python 3 默认就是 UTF-8，但加上也不会错。
- 字符串是**不可变的**！`s[0] = 'H'` 会报错。想要修改字符串，只能创建一个新的。
- `len()` 对 `str` 返回字符数，对 `bytes` 返回字节数。一个中文字符在 UTF-8 里占 3 个字节。

## 🎓 这一关的知识点清单

- **转义字符**：`\n` 换行、`\t` 制表符、`\\` 反斜杠。用 `r'...'` 取消转义。
- **多行字符串**：`'''...'''` 或 `"""..."""` 包裹多行文本。
- **ord()/chr()**：字符和 Unicode 编码之间互相转换。
- **encode()/decode()**：字符串（str）和字节（bytes）之间互相转换，中文用 UTF-8。
- **f-string**：Python 3.6+ 的格式化字符串，`f"...{expr}..."`，简洁强大，推荐首选。

## ➡️ 下一关

字符串搞定了！接下来认识 Python 最常用的数据结构——列表（List），有序、可变、能放任何东西 👉 [下一关：列表 List →](../04-lists/)
