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
