# 第 44 关：StringIO和BytesIO（师兄带你学 Python）

## 🎯 这一关你会学到

- 用 `StringIO` 在内存中读写字符串
- 用 `BytesIO` 在内存中读写字节
- 理解 file-like object 的概念
- 在不需要真实文件时用内存 IO

## 🤔 先想一个问题

有时候你需要「假装」有个文件，但其实数据就在内存里。比如测试代码时不想真创建文件，或者生成 CSV 数据直接发给网络。`StringIO` 和 `BytesIO` 就是内存里的「虚拟文件」。

带着这个问题，我们来看代码。

## 📖 看代码

```python
# StringIO 和 BytesIO

# StringIO：在内存中读写字符串
from io import StringIO

# 写入
f = StringIO()
f.write("Hello")
f.write(" ")
f.write("World!")
print(f.getvalue())    # Hello World!

# 读取（像读文件一样）
f = StringIO("第一行\n第二行\n第三行")
for line in f:
    print(line.strip())

# StringIO 的用途：不需要真文件，在内存里操作
f = StringIO()
f.write("name,age\n")
f.write("Alice,18\n")
f.write("Bob,20\n")
csv_content = f.getvalue()
print(csv_content)

# BytesIO：在内存中读写字节
from io import BytesIO

# 写入
f = BytesIO()
f.write("你好".encode('utf-8'))
print(f.getvalue())    # b'\xe4\xbd\xa0\xe5\xa5\xbd'

# 读取
f = BytesIO(b'\xe4\xbd\xa0\xe5\xa5\xbd')
print(f.read().decode('utf-8'))    # 你好

# StringIO/BytesIO 和普通文件接口一致
# 可以传给任何接受 file-like object 的函数
import json

f = StringIO()
json.dump({'name': 'Alice', 'age': 18}, f, ensure_ascii=False)
print(f.getvalue())    # {"name": "Alice", "age": 18}

f = StringIO('{"name": "Bob", "age": 20}')
data = json.load(f)
print(data)    # {'name': 'Bob', 'age': 20}
```

## 🔍 师兄给你逐行拆

> 代码已经在注释中做了详细说明，这里挑重点讲。

### 核心要点

- `StringIO` 操作字符串，`BytesIO` 操作字节
- `getvalue()` 获取全部内容，不受读写位置影响
- 它们和真实文件接口一样，可以传给任何接受 file-like object 的函数
- `json.dump()` / `json.load()` 都可以用 StringIO 代替文件
- 适合做单元测试：不用创建真实文件就能测试文件处理逻辑

## 🏃 跑一下试试

```bash
cd 44-stringio-bytesio
python stringio-bytesio.py
```

## 💡 师兄的碎碎念

- `StringIO` 操作字符串，`BytesIO` 操作字节
- `getvalue()` 获取全部内容，不受读写位置影响
- 它们和真实文件接口一样，可以传给任何接受 file-like object 的函数
- `json.dump()` / `json.load()` 都可以用 StringIO 代替文件
- 适合做单元测试：不用创建真实文件就能测试文件处理逻辑

## 🎓 这一关的知识点清单

| 知识点 | 说明 |
|--------|------|
| `StringIO()` | 创建内存字符串流 |
| `BytesIO()` | 创建内存字节流 |
| `f.getvalue()` | 获取流中的全部内容 |
| `file-like object` | 有 read/write 方法的对象都可以当文件用 |

## ➡️ 下一关

下一关我们学习 [操作文件和目录](../45-os-operations/README.md)，继续加油！
