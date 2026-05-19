# 文件读写

# 读文件
# 使用 with 自动关闭文件（推荐！）
import os
import tempfile

# 创建临时文件用于演示
tmp_dir = tempfile.mkdtemp()
test_file = os.path.join(tmp_dir, 'test.txt')

# 写入测试文件
with open(test_file, 'w', encoding='utf-8') as f:
    f.write("Hello, Python!\n")
    f.write("你好，世界！\n")
    f.write("第三行内容\n")

# 读取全部内容
with open(test_file, 'r', encoding='utf-8') as f:
    content = f.read()
    print(content)

# 逐行读取
with open(test_file, 'r', encoding='utf-8') as f:
    for line in f:
        print(line.strip())

# 读取所有行到列表
with open(test_file, 'r', encoding='utf-8') as f:
    lines = f.readlines()
    print(lines)

# 写文件
with open(test_file, 'w', encoding='utf-8') as f:
    f.write("覆盖写入\n")

# 追加写入
with open(test_file, 'a', encoding='utf-8') as f:
    f.write("追加内容\n")

with open(test_file, 'r', encoding='utf-8') as f:
    print(f.read())

# 二进制文件
bin_file = os.path.join(tmp_dir, 'test.bin')
with open(bin_file, 'wb') as f:
    f.write(b'\x00\x01\x02\x03')

with open(bin_file, 'rb') as f:
    data = f.read()
    print(data)    # b'\x00\x01\x02\x03'

# 指定编码读取（处理中文常用）
# with open('gbk_file.txt', 'r', encoding='gbk', errors='ignore') as f:
#     content = f.read()

# 清理临时文件
os.remove(test_file)
os.remove(bin_file)
os.rmdir(tmp_dir)
