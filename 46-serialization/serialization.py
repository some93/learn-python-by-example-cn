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
