# StringIO 和 BytesIO

import json
from io import BytesIO, StringIO


print("=== StringIO 写入字符串 ===")

# StringIO 在内存里模拟文本文件，不会真的写到磁盘。
text_io = StringIO()
text_io.write("Hello")
text_io.write(" ")
text_io.write("World!")
print(text_io.getvalue())


print("\n=== 读写位置 seek() ===")

# write 后读写位置在末尾，所以直接 read() 读不到内容。
print(text_io.read())
# seek(0) 把读写位置移动到开头。
text_io.seek(0)
print(text_io.read())


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
print(bytes_io.getvalue())

bytes_io.seek(0)
print(bytes_io.read().decode("utf-8"))


print("\n=== StringIO 作为 file-like object ===")

# json.dump 需要 file-like object，StringIO 正好可以充当这个对象。
json_io = StringIO()
json.dump({"name": "Alice", "age": 18}, json_io, ensure_ascii=False)
print(json_io.getvalue())

json_io = StringIO('{"name": "Bob", "age": 20}')
# json.load 可以从 file-like object 中读取 JSON。
data = json.load(json_io)
print(data["name"])
print(data["age"])
