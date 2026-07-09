# 第 46 关：序列化（师兄带你学 Python）

## 🎯 这一关你会学到

- 什么是序列化和反序列化
- `json.dumps()` / `json.loads()` 处理字符串
- `json.dump()` / `json.load()` 处理文件
- 自定义对象如何转换成 JSON
- JSON 和 pickle 的区别
- 为什么不要反序列化不可信的 pickle 数据

## 🤔 先想一个问题

Python 里的字典、列表、对象都活在内存里。如果你想把它们保存到文件、发给前端、传给别的服务，就得先把它们翻译成通用格式。

把对象变成字符串或字节流，叫序列化。

把字符串或字节流变回对象，叫反序列化。

## 📖 看代码

```python
# 序列化（Serialization）

import json
import pickle
import shutil
from pathlib import Path


print("=== JSON dumps / loads ===")

profile = {
    "name": "Alice",
    "age": 25,
    "skills": ["Python", "Go", "Rust"],
    "address": {"city": "北京", "zip": "100000"},
}

# dumps 把 Python 对象转换成 JSON 字符串。
json_text = json.dumps(profile, ensure_ascii=False, indent=2)
print(json_text)

# loads 把 JSON 字符串解析回 Python 对象。
parsed = json.loads(json_text)
print(parsed["name"])  # Alice
print(parsed["address"]["city"])  # 北京


print("\n=== JSON dump / load 文件 ===")

tmp_dir = Path(__file__).with_name(".tmp-serialization")
tmp_dir.mkdir(exist_ok=True)

try:
    json_file = tmp_dir / "profile.json"
    # dump/load 直接和文件对象配合使用。
    with open(json_file, "w", encoding="utf-8") as file:
        json.dump(profile, file, ensure_ascii=False, indent=2)

    with open(json_file, "r", encoding="utf-8") as file:
        loaded = json.load(file)

    print(loaded["skills"])  # ['Python', 'Go', 'Rust']
finally:
    # 演示结束后清理临时目录。
    try:
        shutil.rmtree(tmp_dir)
    except PermissionError:
        pass


print("\n=== 自定义对象转 JSON ===")


class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age


student = Student("Bob", 20)


def student_to_dict(obj):
    if isinstance(obj, Student):
        # default 函数负责把自定义对象转换成 JSON 支持的类型。
        return {"name": obj.name, "age": obj.age}
    raise TypeError(f"{type(obj).__name__} 不能 JSON 序列化")


print(json.dumps(student, default=student_to_dict, ensure_ascii=False))
print(json.dumps(student, default=lambda obj: obj.__dict__, ensure_ascii=False))


print("\n=== JSON 不支持所有 Python 类型 ===")

try:
    # set 不是 JSON 标准类型，默认无法序列化。
    json.dumps({"numbers": {1, 2, 3}})
except TypeError as error:
    print(type(error).__name__)  # TypeError


print("\n=== pickle dumps / loads ===")

data = {"key": "value", "nums": [1, 2, 3]}
# pickle 会序列化成 bytes，适合 Python 内部临时保存对象。
pickled = pickle.dumps(data)
print(type(pickled).__name__)  # bytes
print(len(pickled) > 0)  # True

unpickled = pickle.loads(pickled)
print(unpickled)  # {'key': 'value', 'nums': [1, 2, 3]}
```

## 🔍 师兄给你逐行拆

### `json.dumps()` 和 `json.loads()`

```python
json_text = json.dumps(profile, ensure_ascii=False, indent=2)
parsed = json.loads(json_text)
```

**这行在干嘛？**

`json.dumps()` 把 Python 对象转成 JSON 字符串。

`json.loads()` 把 JSON 字符串转回 Python 对象。

**参数是什么意思？**

- `ensure_ascii=False`：中文正常显示，不转成 `\u4f60` 这种形式；
- `indent=2`：格式化缩进，方便阅读。

---

### `dump()` 和 `load()` 操作文件

```python
with open(json_file, "w", encoding="utf-8") as file:
    json.dump(profile, file, ensure_ascii=False, indent=2)

with open(json_file, "r", encoding="utf-8") as file:
    loaded = json.load(file)
```

**这行在干嘛？**

`dump()` 少一个 `s`，表示直接写入文件对象。

`load()` 少一个 `s`，表示直接从文件对象读取。

可以这样记：

- `dumps` / `loads`：处理字符串 string；
- `dump` / `load`：处理文件 file。

---

### 自定义对象不能直接 JSON 序列化

```python
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
```

**这行在干嘛？**

普通字典、列表、字符串、数字可以直接转 JSON，但自定义对象 `Student` 不行。

因为 JSON 不知道你的对象应该怎么表示。

---

### `default=` 提供转换函数

```python
def student_to_dict(obj):
    if isinstance(obj, Student):
        return {"name": obj.name, "age": obj.age}
    raise TypeError(f"{type(obj).__name__} 不能 JSON 序列化")


print(json.dumps(student, default=student_to_dict, ensure_ascii=False))
```

**这行在干嘛？**

当 `json.dumps()` 遇到不能处理的对象时，会调用 `default` 函数。我们把 `Student` 转成普通字典，JSON 就能处理了。

**为什么转换函数里要 raise TypeError？**

如果传进来的是别的未知对象，应该明确报错，而不是悄悄返回奇怪结果。

---

### `obj.__dict__` 简写法

```python
json.dumps(student, default=lambda obj: obj.__dict__, ensure_ascii=False)
```

**这行在干嘛？**

很多普通对象的属性存在 `__dict__` 里，所以可以用这个简写。

**容易踩的坑**

不是所有对象都有合适的 `__dict__`，也不是所有属性都应该暴露出去。严肃业务里，明确写转换函数更稳。

---

### JSON 支持的类型有限

```python
try:
    json.dumps({"numbers": {1, 2, 3}})
except TypeError as error:
    print(type(error).__name__)
```

**这行在干嘛？**

JSON 不支持 Python 的 `set`。所以序列化集合会抛 `TypeError`。

常见 JSON 类型对应关系：

| Python | JSON |
|--------|------|
| dict | object |
| list/tuple | array |
| str | string |
| int/float | number |
| True/False | true/false |
| None | null |

---

### pickle：Python 专用二进制序列化

```python
pickled = pickle.dumps(data)
unpickled = pickle.loads(pickled)
```

**这行在干嘛？**

`pickle.dumps()` 把 Python 对象序列化成 bytes。

`pickle.loads()` 把 bytes 反序列化回 Python 对象。

**pickle 和 JSON 怎么选？**

- JSON：跨语言、可读、适合配置/API/数据交换；
- pickle：Python 专用、二进制、能处理更多 Python 对象。

**安全提醒**

不要加载不可信来源的 pickle。pickle 反序列化可能执行恶意代码。

## 🏃 跑一下试试

```bash
$ python serialization.py
=== JSON dumps / loads ===
{
  "name": "Alice",
  "age": 25,
  "skills": [
    "Python",
    "Go",
    "Rust"
  ],
  "address": {
    "city": "北京",
    "zip": "100000"
  }
}
Alice
北京

=== JSON dump / load 文件 ===
['Python', 'Go', 'Rust']

=== 自定义对象转 JSON ===
{"name": "Bob", "age": 20}
{"name": "Bob", "age": 20}

=== JSON 不支持所有 Python 类型 ===
TypeError

=== pickle dumps / loads ===
bytes
True
{'key': 'value', 'nums': [1, 2, 3]}
```

## 💡 师兄的碎碎念

- `dumps/loads` 处理字符串，`dump/load` 处理文件对象。
- `ensure_ascii=False` 可以让中文直接显示。
- 自定义对象要先转成 JSON 支持的基础类型。
- JSON 是跨语言通用格式，pickle 是 Python 专用格式。
- 不要反序列化不可信的 pickle 数据，这是安全红线。

## 🎓 这一关的知识点清单

- **序列化**：把对象转成字符串或字节流。
- **反序列化**：把字符串或字节流转回对象。
- **json.dumps/loads**：JSON 字符串转换。
- **json.dump/load**：JSON 文件读写。
- **default 参数**：提供自定义对象转换函数。
- **pickle**：Python 专用二进制序列化工具。
- **安全风险**：pickle 不适合处理不可信输入。

## ➡️ 下一关

IO 编程到这里收尾。下一关进入并发：先看多进程，理解 Python 如何让多个进程同时干活 👉 [下一关：多进程 →](../47-multiprocessing/)


