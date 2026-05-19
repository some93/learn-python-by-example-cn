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
