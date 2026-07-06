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
print(parsed["name"])
print(parsed["address"]["city"])


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

    print(loaded["skills"])
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
    print(type(error).__name__)


print("\n=== pickle dumps / loads ===")

data = {"key": "value", "nums": [1, 2, 3]}
# pickle 会序列化成 bytes，适合 Python 内部临时保存对象。
pickled = pickle.dumps(data)
print(type(pickled).__name__)
print(len(pickled) > 0)

unpickled = pickle.loads(pickled)
print(unpickled)
