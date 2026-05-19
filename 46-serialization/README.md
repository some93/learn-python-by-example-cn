# 第 46 关：序列化（师兄带你学 Python）

## 🎯 这一关你会学到

- 理解序列化和反序列化的概念
- 用 `json` 模块处理 JSON 数据
- 自定义对象的 JSON 序列化
- 了解 `pickle` 模块

## 🤔 先想一个问题

程序里的字典、列表等数据结构想保存到文件或发给别的程序，直接存不了——得先「翻译」成字符串或字节流。这个翻译过程就叫**序列化**。

带着这个问题，我们来看代码。

## 📖 看代码

```python
# 序列化（Serialization）

import json
import pickle

# JSON 序列化
d = {
    'name': 'Alice',
    'age': 25,
    'skills': ['Python', 'Go', 'Rust'],
    'address': {'city': '北京', 'zip': '100000'}
}

# 序列化为 JSON 字符串
json_str = json.dumps(d, ensure_ascii=False, indent=2)
print(json_str)

# 反序列化
parsed = json.loads(json_str)
print(parsed['name'])
print(parsed['skills'])

# 序列化到文件 / 从文件反序列化
import tempfile, os
tmp = tempfile.mktemp(suffix='.json')

with open(tmp, 'w', encoding='utf-8') as f:
    json.dump(d, f, ensure_ascii=False, indent=2)

with open(tmp, 'r', encoding='utf-8') as f:
    data = json.load(f)
    print(data)

os.remove(tmp)

# 自定义对象的 JSON 序列化
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

s = Student('Bob', 20)

# 默认不能序列化自定义对象，需要转换函数
def student_to_dict(s):
    return {'name': s.name, 'age': s.age}

print(json.dumps(s, default=student_to_dict))

# 通用方法：用 __dict__
print(json.dumps(s, default=lambda obj: obj.__dict__))

# pickle：Python 专用的序列化（二进制）
data = {'key': 'value', 'nums': [1, 2, 3]}
pickled = pickle.dumps(data)
print(type(pickled))    # <class 'bytes'>

unpickled = pickle.loads(pickled)
print(unpickled)

# pickle 可以序列化任何 Python 对象，但只能在 Python 之间用
# JSON 是跨语言的通用格式
```

## 🔍 师兄给你逐行拆

> 代码已经在注释中做了详细说明，这里挑重点讲。

### 核心要点

- `json.dumps()` 序列化为字符串，`json.loads()` 反序列化
- `json.dump()` / `json.load()` 直接操作文件
- `ensure_ascii=False` 让中文正常显示，别忘了加
- 自定义对象用 `default=lambda obj: obj.__dict__` 序列化
- `pickle` 是 Python 专用格式，跨语言请用 JSON

## 🏃 跑一下试试

```bash
cd 46-serialization
python serialization.py
```

## 💡 师兄的碎碎念

- `json.dumps()` 序列化为字符串，`json.loads()` 反序列化
- `json.dump()` / `json.load()` 直接操作文件
- `ensure_ascii=False` 让中文正常显示，别忘了加
- 自定义对象用 `default=lambda obj: obj.__dict__` 序列化
- `pickle` 是 Python 专用格式，跨语言请用 JSON

## 🎓 这一关的知识点清单

| 知识点 | 说明 |
|--------|------|
| `json.dumps(obj)` | 序列化为 JSON 字符串 |
| `json.loads(s)` | 反序列化 JSON 字符串 |
| `json.dump/load` | 直接操作文件的序列化/反序列化 |
| `default=func` | 自定义对象的序列化函数 |
| `pickle.dumps/loads` | Python 专用的二进制序列化 |

## ➡️ 下一关

下一关我们学习 [多进程](../47-multiprocessing/README.md)，继续加油！
