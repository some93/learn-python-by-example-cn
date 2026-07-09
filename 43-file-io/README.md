# 第 43 关：文件读写（师兄带你学 Python）

## 🎯 这一关你会学到

- 为什么推荐 `with open(...) as f`
- 文本文件的读写模式：`r`、`w`、`a`
- `read()`、`readline()`、`readlines()` 的区别
- 大文件为什么适合逐行读取
- 二进制文件模式：`rb`、`wb`
- 编码错误为什么会出现，以及如何指定正确编码

## 🤔 先想一个问题

程序运行时，数据都在内存里。程序一结束，内存就清空了。

如果你想把用户输入、日志、配置、计算结果保存下来，就要写进文件。文件操作看似简单，但有两个大坑：忘记关闭文件、编码不一致。

Python 推荐你用 `with open()`，它能自动关闭文件，让代码更稳。

## 📖 看代码

```python
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
```

## 🔍 师兄给你逐行拆

### 临时目录：演示结束自动清理

```python
import shutil
from pathlib import Path

tmp_dir = Path(__file__).with_name(".tmp-file-io")
tmp_dir.mkdir(exist_ok=True)
```

**这行在干嘛？**

在当前章节目录下创建 `.tmp-file-io` 临时目录。教程运行环境有时不允许写系统临时目录，所以这里把演示文件放在项目内。脚本会尽力清理它；如果 Windows 暂时拒绝删除，目录也已经被 `.gitignore` 忽略，不会进入版本控制。

`tmp_dir / "demo.txt"` 用 `pathlib` 拼路径，比手写字符串更清楚。

---

### `with open()` 自动关闭文件

```python
with open(text_file, "w", encoding="utf-8") as file:
    file.write("Hello, Python!\n")
```

**这行在干嘛？**

以写入模式打开文件，并指定编码为 UTF-8。`with` 代码块结束时，Python 会自动关闭文件。

**为什么重要？**

文件不关闭，可能导致内容没完全写入、文件句柄泄漏、Windows 下文件被占用无法删除。

所以新手记住一句：**文件操作优先用 `with open()`**。

---

### 文件模式：`r`、`w`、`a`

| 模式 | 含义 | 文件不存在 | 原内容 |
|------|------|------------|--------|
| `r` | 读取 | 报错 | 保留 |
| `w` | 写入 | 创建 | 清空 |
| `a` | 追加 | 创建 | 保留并写到末尾 |
| `rb` | 二进制读取 | 报错 | 保留 |
| `wb` | 二进制写入 | 创建 | 清空 |

**容易踩的坑**

`w` 会覆盖原文件。你只是想追加日志时，要用 `a`。

---

### `read()`：一次读完

```python
with open(text_file, "r", encoding="utf-8") as file:
    content = file.read()
    print(content, end="")
```

**这行在干嘛？**

`read()` 一次性读取文件全部内容，返回一个字符串。

**什么时候用？**

小文件可以。大文件不建议一次性读完，否则内存压力很大。

---

### `readline()`：一次一行

```python
print(file.readline().strip())
print(file.readline().strip())
```

**这行在干嘛？**

`readline()` 每次读取一行。行尾通常带 `\n`，所以这里用 `.strip()` 去掉两边空白。

**注意**

如果文件已经读到末尾，`readline()` 会返回空字符串 `""`。

---

### `for line in file`：大文件推荐

```python
with open(text_file, "r", encoding="utf-8") as file:
    for line in file:
        print(line.strip())
```

**这行在干嘛？**

文件对象本身可迭代。用 `for line in file` 会逐行读取，不会一次性把整个文件塞进内存。

大文件日志分析、CSV 逐行处理，都优先用这种方式。

---

### `readlines()`：读成列表

```python
with open(text_file, "r", encoding="utf-8") as file:
    print(file.readlines())
```

**这行在干嘛？**

`readlines()` 把所有行读成列表，每个元素是一行字符串，通常保留换行符。

**容易踩的坑**

它也会一次性读入内存。大文件别用。

---

### 二进制文件

```python
with open(bin_file, "wb") as file:
    file.write(b"\x00\x01\x02\x03")

with open(bin_file, "rb") as file:
    print(file.read())
```

**这行在干嘛？**

`wb` 写入 bytes，`rb` 读取 bytes。图片、音频、压缩包都属于二进制文件。

文本模式处理的是 `str`，二进制模式处理的是 `bytes`。

---

### 编码错误

```python
gbk_file.write_bytes("你好".encode("gbk"))

try:
    with open(gbk_file, "r", encoding="utf-8") as file:
        print(file.read())
except UnicodeDecodeError as error:
    print(type(error).__name__)
```

**这行在干嘛？**

我们故意写入 GBK 编码的中文，再用 UTF-8 去读，于是触发 `UnicodeDecodeError`。

用正确编码读取：

```python
with open(gbk_file, "r", encoding="gbk") as file:
    print(file.read())
```

就能正常得到 `你好`。

**现实建议**

新项目统一用 UTF-8。遇到历史文件时，先确认编码，再决定 `encoding="gbk"`、`encoding="utf-8"`，不要盲猜。

## 🏃 跑一下试试

```bash
$ python file-io.py
=== 写入文本文件 ===
demo.txt
True

=== read() 读取全部内容 ===
Hello, Python!
你好，世界！
第三行内容

=== readline() 每次读一行 ===
Hello, Python!
你好，世界！

=== for line in file 逐行读取 ===
Hello, Python!
你好，世界！
第三行内容

=== readlines() 读取为列表 ===
['Hello, Python!\n', '你好，世界！\n', '第三行内容\n']

=== w 覆盖写入，a 追加写入 ===
覆盖写入
追加内容

=== 二进制文件 ===
b'\x00\x01\x02\x03'

=== 编码错误处理 ===
UnicodeDecodeError
你好
```

## 💡 师兄的碎碎念

- 文件读写优先用 `with open()`，自动关闭最省心。
- 文本文件要指定 `encoding`，中文项目优先 UTF-8。
- `read()` 和 `readlines()` 都会一次性读入内存，大文件慎用。
- 逐行处理大文件时，用 `for line in file`。
- `w` 会覆盖，`a` 会追加；写日志通常用 `a`。

## 🎓 这一关的知识点清单

- **open()**：打开文件，返回文件对象。
- **with**：上下文管理器，自动关闭文件。
- **read/readline/readlines**：三种读取方式。
- **write()**：写入字符串或 bytes。
- **文件模式**：`r/w/a/rb/wb` 控制读写和文本/二进制。
- **encoding**：指定文本编码，避免中文乱码。
- **UnicodeDecodeError**：用错误编码读取文本时常见异常。

## ➡️ 下一关

文件在磁盘上，下一关看内存里的“文件”：`StringIO` 和 `BytesIO`，不落盘也能像文件一样读写 👉 [下一关：StringIO 和 BytesIO →](../44-stringio-bytesio/)


