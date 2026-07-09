# 第 45 关：操作文件和目录

## 🎯 这一关你会学到

- `os.path` 如何拼接、拆分路径
- `pathlib.Path` 的现代路径写法
- 创建目录、创建文件、重命名、删除文件
- 遍历和筛选目录内容
- `os.walk()` 递归遍历目录树
- `shutil` 如何复制文件和删除目录树

## 🤔 先想一个问题

你想写个脚本整理下载文件夹：`.jpg` 放图片目录，`.pdf` 放文档目录，临时文件删掉。

这类任务的第一步，就是会用 Python 操作文件和目录：拼路径、判断文件是否存在、列目录、复制、重命名、删除。

## 📖 看代码

```python
# 操作文件和目录

import os
import shutil
from pathlib import Path


print("=== 路径拼接和拆分 ===")

# os.path.join 会按当前系统使用正确的路径分隔符。
path = os.path.join("downloads", "images", "cat.jpg")
print(path)  # downloads/images/cat.jpg
print(os.path.split(path))  # ('downloads/images', 'cat.jpg')
print(os.path.splitext(path))  # ('downloads/images/cat', '.jpg')

p = Path("downloads") / "docs" / "readme.txt"
# pathlib 用 / 拼路径，可读性比字符串拼接更好。
print(p.as_posix())  # downloads/docs/readme.txt
print(p.name)  # readme.txt
print(p.suffix)  # .txt
print(p.stem)  # readme


print("\n=== 创建目录和文件 ===")

base_dir = Path(__file__).with_name(".tmp-os-operations")
if base_dir.exists():
    try:
        # 每次运行前清理旧目录，保证输出稳定。
        shutil.rmtree(base_dir)
    except PermissionError:
        pass
base_dir.mkdir(exist_ok=True)

try:
    images_dir = base_dir / "images"
    docs_dir = base_dir / "docs"
    # mkdir 创建目录，exist_ok=True 表示目录已存在也不报错。
    images_dir.mkdir(exist_ok=True)
    docs_dir.mkdir(exist_ok=True)

    cat_file = images_dir / "cat.jpg"
    readme_file = docs_dir / "readme.txt"
    # pathlib 提供了便捷的文本和字节写入方法。
    cat_file.write_bytes(b"fake image")
    readme_file.write_text("hello\n", encoding="utf-8")

    print(images_dir.is_dir())  # True
    print(cat_file.is_file())  # True

    print("\n=== 列出目录内容 ===")
    # iterdir 列出当前目录的直接子项。
    print(sorted(item.name for item in base_dir.iterdir()))  # ['docs', 'images']
    print(sorted(item.name for item in base_dir.iterdir() if item.is_dir()))  # ['docs', 'images']
    print(sorted(item.name for item in docs_dir.glob("*.txt")))  # ['guide.txt', 'readme.txt']

    print("\n=== 复制文件（演示更稳定） ===")
    guide_file = docs_dir / "guide.txt"
    # shutil.copy 复制文件内容和权限信息中的一部分。
    shutil.copy(readme_file, guide_file)
    print(guide_file.exists())  # True
    print(guide_file.read_text(encoding="utf-8").strip())  # hello

    print("\n=== os.walk 递归遍历 ===")
    all_files = []
    # os.walk 会递归产出目录路径、子目录名、文件名。
    for dirpath, dirnames, filenames in os.walk(base_dir):
        for filename in filenames:
            full_path = Path(dirpath) / filename
            all_files.append(full_path.relative_to(base_dir).as_posix())
    print(sorted(all_files))  # ['docs/guide.txt', 'docs/readme.txt', 'images/cat.jpg']

    print("\n=== shutil 复制文件到根目录 ===")
    copy_file = base_dir / "cat-copy.jpg"
    shutil.copy(cat_file, copy_file)
    print(copy_file.exists())  # True
finally:
    # 清理演示目录；权限受限时忽略，避免影响教程运行。
    try:
        shutil.rmtree(base_dir)
    except PermissionError:
        pass
```

## 🔍 师兄给你逐行拆

### `os.path`：老牌路径工具

```python
path = os.path.join("downloads", "images", "cat.jpg")
print(os.path.split(path))
print(os.path.splitext(path))
```

**这行在干嘛？**

`os.path.join()` 按当前系统规则拼接路径。Windows 用反斜杠，Linux/macOS 用斜杠。

`os.path.split()` 拆出目录和文件名。

`os.path.splitext()` 拆出主路径和扩展名。

**为什么别用字符串硬拼？**

手写 `"downloads/images/cat.jpg"` 在多数时候能跑，但跨平台和边界情况更容易出错。路径交给路径工具拼。

---

### `pathlib.Path`：现代推荐写法

```python
p = Path("downloads") / "docs" / "readme.txt"
print(p.as_posix())
print(p.name)
print(p.suffix)
print(p.stem)
```

**这行在干嘛？**

`Path` 用 `/` 运算符拼路径，读起来很自然。

- `p.name`：文件名 `readme.txt`
- `p.suffix`：扩展名 `.txt`
- `p.stem`：不带扩展名的文件名 `readme`

**实际建议**

新项目优先用 `pathlib`。遇到老代码或某些库接口时，再用 `os.path`。

---

### 创建目录和文件

```python
base_dir = Path(__file__).with_name(".tmp-os-operations")
base_dir.mkdir(exist_ok=True)

images_dir.mkdir(exist_ok=True)
cat_file.write_bytes(b"fake image")
readme_file.write_text("hello\n", encoding="utf-8")
```

**这行在干嘛？**

在当前章节目录下创建演示目录 `.tmp-os-operations`，再创建子目录和文件。

`write_text()` 写文本，`write_bytes()` 写二进制。

**为什么不用系统临时目录？**

有些受限运行环境不允许写系统临时目录。教程示例放在项目内，并用 `.gitignore` 忽略 `.tmp-*` 目录，运行更稳定。

---

### 列出目录内容

```python
print(sorted(item.name for item in base_dir.iterdir()))
print(sorted(item.name for item in base_dir.iterdir() if item.is_dir()))
print(sorted(item.name for item in docs_dir.glob("*.txt")))
```

**这行在干嘛？**

`iterdir()` 列出当前目录下一层内容。

`item.is_dir()` 判断是不是目录。

`glob("*.txt")` 按通配符筛选 `.txt` 文件。

**容易踩的坑**

`iterdir()` 只看一层，不递归。要递归可以用 `rglob()` 或 `os.walk()`。

---

### 复制、重命名和删除

```python
guide_file = docs_dir / "guide.txt"
shutil.copy(readme_file, guide_file)
print(guide_file.exists())
```

**这行在干嘛？**

示例里用 `shutil.copy()` 复制文件，输出更稳定。真实项目里也常用这些操作：

```python
readme_file.rename(docs_dir / "guide.txt")  # 重命名或移动
readme_file.unlink()                        # 删除文件
```

**注意**

删除目录不能用 `unlink()`，目录要用 `rmdir()` 或 `shutil.rmtree()`。删除和移动都属于破坏性操作，脚本里一定先确认路径。

---

### `os.walk()` 递归遍历

```python
for dirpath, dirnames, filenames in os.walk(base_dir):
    for filename in filenames:
        ...
```

**这行在干嘛？**

`os.walk()` 会递归遍历目录树，每次返回：

```python
(当前目录路径, 子目录名列表, 文件名列表)
```

适合做批量扫描、文件分类、统计目录大小等任务。

---

### `shutil` 负责复制和目录树操作

```python
shutil.copy(cat_file, copy_file)
```

**这行在干嘛？**

`os` 模块偏基础文件系统操作，复制文件、复制目录树、删除整个目录树通常用 `shutil`。

常用：

```python
shutil.copy(src, dst)
shutil.copytree(src_dir, dst_dir)
shutil.rmtree(dir_path)
```

**危险提醒**

`shutil.rmtree()` 会递归删除整个目录树。写脚本时一定确认路径，别对用户目录或项目根目录误删。

## 🏃 跑一下试试

```bash
$ python os-operations.py
=== 路径拼接和拆分 ===
downloads\images\cat.jpg
('downloads\\images', 'cat.jpg')
('downloads\\images\\cat', '.jpg')
downloads/docs/readme.txt
readme.txt
.txt
readme

=== 创建目录和文件 ===
True
True

=== 列出目录内容 ===
['docs', 'images']
['docs', 'images']
['readme.txt']

=== 复制文件（演示更稳定） ===
True
hello

=== os.walk 递归遍历 ===
['docs/guide.txt', 'docs/readme.txt', 'images/cat.jpg']

=== shutil 复制文件到根目录 ===
True
```

## 💡 师兄的碎碎念

- 新代码优先用 `pathlib.Path`，老代码里常见 `os.path`。
- 拼路径不要手写字符串连接，跨平台容易出问题。
- `Path.unlink()` 删除文件，`Path.rmdir()` 删除空目录。
- 递归遍历用 `os.walk()` 或 `Path.rglob()`。
- 复制文件、复制目录、删除目录树用 `shutil`。

## 🎓 这一关的知识点清单

- **os.path.join/split/splitext**：传统路径拼接和拆分工具。
- **Path**：现代路径对象，支持 `/` 拼接路径。
- **mkdir/write_text/write_bytes**：创建目录和写文件。
- **iterdir/glob**：列出和筛选目录内容。
- **rename/unlink**：重命名和删除文件，属于需要谨慎使用的破坏性操作。
- **os.walk**：递归遍历目录树。
- **shutil**：复制文件、复制目录、删除目录树。

## ➡️ 下一关

文件和目录会操作了，下一关看序列化：如何把 Python 对象变成 JSON 字符串或字节流保存起来 👉 [下一关：序列化 →](../46-serialization/)


