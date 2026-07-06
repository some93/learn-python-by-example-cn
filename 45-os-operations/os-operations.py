# 操作文件和目录

import os
import shutil
from pathlib import Path


print("=== 路径拼接和拆分 ===")

# os.path.join 会按当前系统使用正确的路径分隔符。
path = os.path.join("downloads", "images", "cat.jpg")
print(path)
print(os.path.split(path))
print(os.path.splitext(path))

p = Path("downloads") / "docs" / "readme.txt"
# pathlib 用 / 拼路径，可读性比字符串拼接更好。
print(p.as_posix())
print(p.name)
print(p.suffix)
print(p.stem)


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

    print(images_dir.is_dir())
    print(cat_file.is_file())

    print("\n=== 列出目录内容 ===")
    # iterdir 列出当前目录的直接子项。
    print(sorted(item.name for item in base_dir.iterdir()))
    print(sorted(item.name for item in base_dir.iterdir() if item.is_dir()))
    print(sorted(item.name for item in docs_dir.glob("*.txt")))

    print("\n=== 复制文件（演示更稳定） ===")
    guide_file = docs_dir / "guide.txt"
    # shutil.copy 复制文件内容和权限信息中的一部分。
    shutil.copy(readme_file, guide_file)
    print(guide_file.exists())
    print(guide_file.read_text(encoding="utf-8").strip())

    print("\n=== os.walk 递归遍历 ===")
    all_files = []
    # os.walk 会递归产出目录路径、子目录名、文件名。
    for dirpath, dirnames, filenames in os.walk(base_dir):
        for filename in filenames:
            full_path = Path(dirpath) / filename
            all_files.append(full_path.relative_to(base_dir).as_posix())
    print(sorted(all_files))

    print("\n=== shutil 复制文件到根目录 ===")
    copy_file = base_dir / "cat-copy.jpg"
    shutil.copy(cat_file, copy_file)
    print(copy_file.exists())
finally:
    # 清理演示目录；权限受限时忽略，避免影响教程运行。
    try:
        shutil.rmtree(base_dir)
    except PermissionError:
        pass
