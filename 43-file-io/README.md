# 第 43 关：文件读写（师兄带你学 Python）

## 🎯 这一关你会学到

- 用 `with open()` 读写文件
- 掌握 `read` / `readline` / `readlines` 的区别
- 写入和追加文件内容
- 处理二进制文件和编码问题

## 🤔 先想一个问题

程序运行时数据都在内存里，一关机就没了。想把数据保存下来？最直接的方式就是写到文件里。但文件操作有个大坑：**忘记关文件**。

带着这个问题，我们来看代码。

## 📖 看代码

```python
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
```

## 🔍 师兄给你逐行拆

> 代码已经在注释中做了详细说明，这里挑重点讲。

### 核心要点

- **永远用 `with open()`**，它会自动关闭文件，不用手动 `f.close()`
- `'r'` 读、`'w'` 写（覆盖）、`'a'` 追加、`'rb'`/`'wb'` 二进制
- 读中文文件一定要指定 `encoding='utf-8'`
- `errors='ignore'` 可以跳过编码错误，但可能丢数据
- 大文件用 `for line in f` 逐行读取，别用 `read()` 一次全读进内存

## 🏃 跑一下试试

```bash
cd 43-file-io
python file-io.py
```

## 💡 师兄的碎碎念

- **永远用 `with open()`**，它会自动关闭文件，不用手动 `f.close()`
- `'r'` 读、`'w'` 写（覆盖）、`'a'` 追加、`'rb'`/`'wb'` 二进制
- 读中文文件一定要指定 `encoding='utf-8'`
- `errors='ignore'` 可以跳过编码错误，但可能丢数据
- 大文件用 `for line in f` 逐行读取，别用 `read()` 一次全读进内存

## 🎓 这一关的知识点清单

| 知识点 | 说明 |
|--------|------|
| `with open(f, 'r') as f` | 安全打开文件的方式 |
| `f.read()` | 读取全部内容 |
| `f.readlines()` | 读取所有行到列表 |
| `f.write(str)` | 写入字符串 |
| `encoding='utf-8'` | 指定文件编码 |
| `'rb' / 'wb'` | 二进制读写模式 |

## ➡️ 下一关

下一关我们学习 [StringIO和BytesIO](../44-stringio-bytesio/README.md)，继续加油！
