# 第 44 关：StringIO 和 BytesIO

## 🎯 这一关你会学到

- `StringIO` 如何在内存中模拟文本文件
- `BytesIO` 如何在内存中模拟二进制文件
- `getvalue()` 和 `read()` 的区别
- `seek(0)` 如何移动读写位置
- 什么是 file-like object

## 🤔 先想一个问题

有时候你需要“像操作文件一样操作数据”，但又不想真的创建文件。

比如测试代码时不想污染磁盘，生成 CSV 后直接发给网络，或者把 JSON 写进内存再读取。

`StringIO` 和 `BytesIO` 就是内存里的虚拟文件。

## 📖 看代码

```python
# StringIO 和 BytesIO

import json
from io import BytesIO, StringIO


print("=== StringIO 写入字符串 ===")

# StringIO 在内存里模拟文本文件，不会真的写到磁盘。
text_io = StringIO()
text_io.write("Hello")
text_io.write(" ")
text_io.write("World!")
print(text_io.getvalue())  # Hello World!


print("\n=== 读写位置 seek() ===")

# write 后读写位置在末尾，所以直接 read() 读不到内容。
print(text_io.read())  # 
# seek(0) 把读写位置移动到开头。
text_io.seek(0)
print(text_io.read())  # Hello World!


print("\n=== StringIO 逐行读取 ===")

text_io = StringIO("第一行\n第二行\n第三行")
# StringIO 和真实文件一样可以逐行迭代。
for line in text_io:
    print(line.strip())


print("\n=== 用 StringIO 生成 CSV 文本 ===")

# 先在内存中拼出文本，最后一次性取出完整内容。
csv_io = StringIO()
csv_io.write("name,age\n")
csv_io.write("Alice,18\n")
csv_io.write("Bob,20\n")
print(csv_io.getvalue(), end="")


print("\n=== BytesIO 写入字节 ===")

# BytesIO 处理的是 bytes，不是 str。
bytes_io = BytesIO()
bytes_io.write("你好".encode("utf-8"))
print(bytes_io.getvalue())  # b'\xe4\xbd\xa0\xe5\xa5\xbd'

bytes_io.seek(0)
print(bytes_io.read().decode("utf-8"))  # 你好


print("\n=== StringIO 作为 file-like object ===")

# json.dump 需要 file-like object，StringIO 正好可以充当这个对象。
json_io = StringIO()
json.dump({"name": "Alice", "age": 18}, json_io, ensure_ascii=False)
print(json_io.getvalue())

json_io = StringIO('{"name": "Bob", "age": 20}')
# json.load 可以从 file-like object 中读取 JSON。
data = json.load(json_io)
print(data["name"])  # Bob
print(data["age"])  # 20
```

## 🔍 师兄给你逐行拆

### `StringIO`：内存里的文本文件

```python
text_io = StringIO()
text_io.write("Hello")
text_io.write(" ")
text_io.write("World!")
print(text_io.getvalue())
```

**这行在干嘛？**

`StringIO()` 创建一个内存文本流。你可以像写文件一样 `.write()` 字符串。

`getvalue()` 会拿到当前内存流里的全部内容：

```python
Hello World!
```

**为什么不用真实文件？**

因为数据只需要临时存在内存里，不需要落盘。这样速度快，也不会产生临时文件。

---

### `read()` 受当前位置影响，`getvalue()` 不受

```python
print(text_io.read())
text_io.seek(0)
print(text_io.read())
```

**这行在干嘛？**

写完内容后，读写位置在末尾。此时直接 `read()`，读不到东西，所以输出空行。

`seek(0)` 把位置移动到开头，再 `read()` 才能读出完整内容。

**容易踩的坑**

`StringIO` 和真实文件一样有“当前位置”。写完想读，记得 `seek(0)`。

`getvalue()` 不看当前位置，直接返回全部内容。

---

### 逐行读取

```python
text_io = StringIO("第一行\n第二行\n第三行")
for line in text_io:
    print(line.strip())
```

**这行在干嘛？**

`StringIO` 像文件对象一样可迭代，所以可以逐行读取。

这说明它是 file-like object：长得不像真实文件，但有类似文件的接口。

---

### 用 `StringIO` 生成 CSV 文本

```python
csv_io = StringIO()
csv_io.write("name,age\n")
csv_io.write("Alice,18\n")
csv_io.write("Bob,20\n")
print(csv_io.getvalue(), end="")
```

**这行在干嘛？**

在内存里拼出一段 CSV 文本，不创建真实 `.csv` 文件。

真实项目里，你可以把这段文本直接返回给浏览器下载，或者传给下游接口。

---

### `BytesIO`：内存里的二进制文件

```python
bytes_io = BytesIO()
bytes_io.write("你好".encode("utf-8"))
print(bytes_io.getvalue())
```

**这行在干嘛？**

`BytesIO` 只能写入 `bytes`，所以中文字符串要先 `.encode("utf-8")`。

输出是 UTF-8 编码后的字节：

```python
b'\xe4\xbd\xa0\xe5\xa5\xbd'
```

**StringIO 和 BytesIO 怎么选？**

- 文本数据：`StringIO`
- 二进制数据：`BytesIO`

---

### file-like object

```python
json_io = StringIO()
json.dump({"name": "Alice", "age": 18}, json_io, ensure_ascii=False)
print(json_io.getvalue())
```

**这行在干嘛？**

`json.dump()` 需要一个“像文件一样能写”的对象。`StringIO` 有 `.write()`，所以可以直接传进去。

同理，`json.load()` 需要一个能 `.read()` 的对象，`StringIO` 也可以胜任。

**为什么这个概念重要？**

Python 很多库不要求你传真实文件，只要求对象有 `read()` 或 `write()` 方法。这让测试和内存处理非常方便。

## 🏃 跑一下试试

```bash
$ python stringio-bytesio.py
=== StringIO 写入字符串 ===
Hello World!

=== 读写位置 seek() ===

Hello World!

=== StringIO 逐行读取 ===
第一行
第二行
第三行

=== 用 StringIO 生成 CSV 文本 ===
name,age
Alice,18
Bob,20

=== BytesIO 写入字节 ===
b'\xe4\xbd\xa0\xe5\xa5\xbd'
你好

=== StringIO 作为 file-like object ===
{"name": "Alice", "age": 18}
Bob
20
```

## 💡 师兄的碎碎念

- `StringIO` 处理 `str`，`BytesIO` 处理 `bytes`。
- 写完再读时，通常要先 `seek(0)` 回到开头。
- `getvalue()` 返回全部内容，不受当前位置影响。
- file-like object 不一定是真文件，只要有 `read()` / `write()` 等接口就能被很多库使用。
- 单元测试里经常用 `StringIO` / `BytesIO` 代替真实文件，测试更快也更干净。

## 🎓 这一关的知识点清单

- **StringIO**：内存文本流，读写字符串。
- **BytesIO**：内存字节流，读写 bytes。
- **getvalue()**：获取内存流全部内容。
- **seek()**：移动读写位置。
- **file-like object**：拥有文件式接口的对象。
- **encode/decode**：字符串和字节之间转换。

## ➡️ 下一关

内存 IO 搞定后，下一关回到真实文件系统：创建目录、列文件、重命名、删除、拼路径 👉 [下一关：操作文件和目录 →](../45-os-operations/)


