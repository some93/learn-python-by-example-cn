# 文件读写

import shutil
from pathlib import Path


print("=== 写入文本文件 ===")

tmp_dir = Path(__file__).with_name(".tmp-file-io")
tmp_dir.mkdir(exist_ok=True)
# 先清空旧文件，保证每次运行输出一致。
for old_file in tmp_dir.iterdir():
    if old_file.is_file():
        try:
            old_file.unlink()
        except PermissionError:
            pass

try:
    text_file = tmp_dir / "demo.txt"

    # with 会自动关闭文件，即使中途发生异常也能释放资源。
    with open(text_file, "w", encoding="utf-8") as file:
        file.write("Hello, Python!\n")
        file.write("你好，世界！\n")
        file.write("第三行内容\n")

    print(text_file.name)  # demo.txt
    print(text_file.exists())  # True

    print("\n=== read() 读取全部内容 ===")
    with open(text_file, "r", encoding="utf-8") as file:
        # read() 一次性读取全部内容，适合小文件。
        content = file.read()
        print(content, end="")

    print("\n=== readline() 每次读一行 ===")
    with open(text_file, "r", encoding="utf-8") as file:
        # readline() 每次读取一行，返回内容包含换行符。
        print(file.readline().strip())
        print(file.readline().strip())

    print("\n=== for line in file 逐行读取 ===")
    with open(text_file, "r", encoding="utf-8") as file:
        # 文件对象本身可迭代，适合逐行处理大文件。
        for line in file:
            print(line.strip())

    print("\n=== readlines() 读取为列表 ===")
    with open(text_file, "r", encoding="utf-8") as file:
        print(file.readlines())

    print("\n=== w 覆盖写入，a 追加写入 ===")
    # w 会覆盖原文件内容。
    with open(text_file, "w", encoding="utf-8") as file:
        file.write("覆盖写入\n")

    # a 会把新内容追加到文件末尾。
    with open(text_file, "a", encoding="utf-8") as file:
        file.write("追加内容\n")

    with open(text_file, "r", encoding="utf-8") as file:
        print(file.read(), end="")

    print("\n=== 二进制文件 ===")
    bin_file = Path(tmp_dir) / "demo.bin"

    # 二进制模式读写 bytes，常用于图片、音频、压缩包等文件。
    with open(bin_file, "wb") as file:
        file.write(b"\x00\x01\x02\x03")

    with open(bin_file, "rb") as file:
        print(file.read())  # b'\x00\x01\x02\x03'

    print("\n=== 编码错误处理 ===")
    gbk_file = Path(tmp_dir) / "gbk.txt"
    gbk_file.write_bytes("你好".encode("gbk"))

    try:
        # 用错误编码读取文件会触发 UnicodeDecodeError。
        with open(gbk_file, "r", encoding="utf-8") as file:
            print(file.read())
    except UnicodeDecodeError as error:
        print(type(error).__name__)  # UnicodeDecodeError

    with open(gbk_file, "r", encoding="gbk") as file:
        print(file.read())  # 你好
finally:
    # 清理演示文件；Windows 沙箱偶尔会拒绝删除，所以这里容错。
    try:
        shutil.rmtree(tmp_dir)
    except PermissionError:
        pass
