# 第 45 关：操作文件和目录（师兄带你学 Python）

## 🎯 这一关你会学到

- 用 `os.path` 操作路径
- 用 `pathlib.Path` 操作路径（推荐）
- 创建、删除文件和目录
- 遍历和筛选目录内容

## 🤔 先想一个问题

你想写个脚本批量整理下载文件夹：把 .jpg 放一个文件夹，.pdf 放另一个。首先你得知道怎么用 Python 操作文件和目录。

带着这个问题，我们来看代码。

## 📖 看代码

```python
# 操作文件和目录

import os

# 环境变量
print(os.name)                      # posix / nt
print(os.environ.get('PATH', ''))   # PATH 环境变量

# 路径操作（推荐用 os.path）
print(os.path.abspath('.'))         # 当前目录的绝对路径
print(os.path.join('/tmp', 'test', 'file.txt'))  # 拼接路径
print(os.path.split('/tmp/test/file.txt'))       # ('/tmp/test', 'file.txt')
print(os.path.splitext('/tmp/test/file.txt'))     # ('/tmp/test/file', '.txt')

# 更推荐用 pathlib（Python 3.4+）
from pathlib import Path

p = Path('.')
print(p.resolve())          # 绝对路径
print(p / 'sub' / 'file')   # 拼接路径（用 / 运算符！）

# 目录操作
import tempfile

tmp = tempfile.mkdtemp()
test_dir = os.path.join(tmp, 'mydir')

os.mkdir(test_dir)                    # 创建目录
print(os.path.isdir(test_dir))        # True

# 创建和删除文件
test_file = os.path.join(test_dir, 'test.txt')
with open(test_file, 'w') as f:
    f.write('hello')

print(os.path.isfile(test_file))     # True

os.remove(test_file)                 # 删除文件
os.rmdir(test_dir)                   # 删除空目录

# 列出目录内容
print([x for x in os.listdir('.') if os.path.isdir(x)])   # 只列子目录
print([x for x in os.listdir('.') if os.path.isfile(x)])  # 只列文件

# 用 pathlib 列出所有 .py 文件
py_files = list(Path('.').glob('*.py'))
print(py_files)

# os.walk：递归遍历目录
for dirpath, dirnames, filenames in os.walk('.'):
    for f in filenames:
        if f.endswith('.py'):
            print(os.path.join(dirpath, f))
    break   # 只遍历当前层

# 复制文件需要用 shutil
import shutil
# shutil.copy('src.txt', 'dst.txt')      # 复制文件
# shutil.copytree('src_dir', 'dst_dir')  # 复制整个目录
# shutil.rmtree('dir')                    # 删除整个目录树

# 清理
os.rmdir(tmp)
```

## 🔍 师兄给你逐行拆

> 代码已经在注释中做了详细说明，这里挑重点讲。

### 核心要点

- `os.path.join()` 拼接路径，别用字符串拼接，跨平台更安全
- `pathlib.Path` 是更现代的方式，用 `/` 运算符拼接路径，很优雅
- `os.walk()` 递归遍历目录，返回 (目录路径, 子目录列表, 文件列表)
- 删除操作要小心！`os.remove` 删文件，`os.rmdir` 只能删空目录
- 复制文件用 `shutil.copy()`，`os` 模块没有复制功能

## 🏃 跑一下试试

```bash
cd 45-os-operations
python os-operations.py
```

## 💡 师兄的碎碎念

- `os.path.join()` 拼接路径，别用字符串拼接，跨平台更安全
- `pathlib.Path` 是更现代的方式，用 `/` 运算符拼接路径，很优雅
- `os.walk()` 递归遍历目录，返回 (目录路径, 子目录列表, 文件列表)
- 删除操作要小心！`os.remove` 删文件，`os.rmdir` 只能删空目录
- 复制文件用 `shutil.copy()`，`os` 模块没有复制功能

## 🎓 这一关的知识点清单

| 知识点 | 说明 |
|--------|------|
| `os.path.join()` | 跨平台拼接路径 |
| `os.path.split/splitext` | 分离路径和扩展名 |
| `Path('.') / 'sub'` | pathlib 风格的路径拼接 |
| `os.mkdir / os.rmdir` | 创建/删除目录 |
| `os.walk()` | 递归遍历目录树 |
| `shutil.copy()` | 复制文件 |

## ➡️ 下一关

下一关我们学习 [序列化](../46-serialization/README.md)，继续加油！
