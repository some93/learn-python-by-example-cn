# 第 53 关：base64（师兄带你学 Python）

## 🎯 这一关你会学到

- Base64 是编码，不是加密
- `b64encode()` / `b64decode()` 如何处理 `bytes`
- 字符串为什么要先 `.encode()` 再做 Base64
- URL-safe Base64 和普通 Base64 的区别
- 末尾 `=` padding 是什么，去掉后如何补回
- 如何用 `validate=True` 检查非法输入

## 🤔 先想一个问题

JSON、URL、邮件正文这些文本协议不适合直接塞图片、压缩包、任意二进制字节。Base64 的作用就是：**把 bytes 变成 ASCII 文本，方便放进文本协议里传输**。

但它不是加密。Base64 文本看起来像一串乱码，实际上任何人都可以直接解码。

## 📖 看代码

```python
# base64 编码

import base64
import binascii


print("=== bytes 编码和解码 ===")

# b64encode 接收 bytes，返回的也是 bytes。
raw = b"Hello, Python!"
encoded = base64.b64encode(raw)
decoded = base64.b64decode(encoded)

print(encoded)
print(decoded)
print(decoded == raw)


print("\n=== 字符串需要先转成 bytes ===")

text = "你好，Python"

# 普通字符串要先按 UTF-8 编码成 bytes，再做 Base64。
text_bytes = text.encode("utf-8")
text_token = base64.b64encode(text_bytes).decode("ascii")

print(text_token)
print(base64.b64decode(text_token).decode("utf-8"))


print("\n=== 二进制数据也能转成文本 ===")

# 这几字节可以想象成图片、文件片段或网络协议里的二进制内容。
binary = bytes([0, 255, 16, 32, 128])
binary_token = base64.b64encode(binary).decode("ascii")

print(binary_token)
print(list(base64.b64decode(binary_token)))


print("\n=== URL-safe Base64 ===")

special_bytes = b"\xfb\xef\xff"

# 标准 Base64 可能出现 + 和 /，放进 URL 时不太友好。
standard = base64.b64encode(special_bytes)
url_safe = base64.urlsafe_b64encode(special_bytes)

print(standard)
print(url_safe)
print(base64.urlsafe_b64decode(url_safe))


print("\n=== 去掉 padding 的 URL token ===")

# 很多 token 会去掉末尾的 =，传输前更短，但解码时要补回来。
token = base64.urlsafe_b64encode(b"user:42").decode("ascii").rstrip("=")
padding = "=" * (-len(token) % 4)
restored = base64.urlsafe_b64decode(token + padding)

print(token)
print(restored)


print("\n=== Base64 不是加密 ===")

secret = "password=123456"
visible = base64.b64encode(secret.encode("utf-8")).decode("ascii")

# 任何人拿到 Base64 文本都能反解出来，所以它不能保护秘密。
print(visible)
print(base64.b64decode(visible).decode("utf-8"))


print("\n=== 校验非法 Base64 ===")

try:
    # validate=True 会严格检查输入，不合法就抛 binascii.Error。
    base64.b64decode("not base64!!!", validate=True)
except binascii.Error as error:
    print(type(error).__name__)


print("\n=== 编码体积会变大 ===")

original = b"a" * 100
encoded = base64.b64encode(original)

# Base64 用 4 个字符表示 3 个字节，体积大约增加三分之一。
print(f"原始: {len(original)} 字节")
print(f"编码后: {len(encoded)} 字节")
```

## 🔍 师兄给你拆开讲

`b64encode()` 处理的是 `bytes`，返回也是 `bytes`。如果你要编码普通字符串，要先用 `.encode("utf-8")` 变成字节；如果你要展示 Base64 文本，再用 `.decode("ascii")` 变成字符串。

普通 Base64 字符表里有 `+` 和 `/`。它们放在 URL 里容易和路径、查询参数规则冲突，所以 URL 场景更常用 `urlsafe_b64encode()`，它会把 `+`、`/` 替换成 `-`、`_`。

Base64 末尾的 `=` 叫 padding，用来补齐长度。很多 token 为了更短会去掉 `=`，但解码时长度必须补回 4 的倍数。示例里的 `padding = "=" * (-len(token) % 4)` 就是在计算该补几个 `=`。

默认的 `b64decode()` 对输入比较宽松，可能忽略一些无效字符。处理外部输入时，如果你想严格校验，使用 `validate=True`。

## 🏃 跑一下试试

```bash
cd 53-base64
python base64_demo.py
```

输出：

```text
=== bytes 编码和解码 ===
b'SGVsbG8sIFB5dGhvbiE='
b'Hello, Python!'
True

=== 字符串需要先转成 bytes ===
5L2g5aW977yMUHl0aG9u
你好，Python

=== 二进制数据也能转成文本 ===
AP8QIIA=
[0, 255, 16, 32, 128]

=== URL-safe Base64 ===
b'++//'
b'--__'
b'\xfb\xef\xff'

=== 去掉 padding 的 URL token ===
dXNlcjo0Mg
b'user:42'

=== Base64 不是加密 ===
cGFzc3dvcmQ9MTIzNDU2
password=123456

=== 校验非法 Base64 ===
Error

=== 编码体积会变大 ===
原始: 100 字节
编码后: 136 字节
```

## 💡 师兄的提醒

看到 Base64 不要误判为“加密后的密文”。它只是换了一种文本表示，保护不了密码、Token、隐私数据。

Base64 会让体积变大，适合小段二进制数据嵌入文本协议；大文件还是应该用文件上传、对象存储、流式传输这类方式。

## 🎓 这一关的知识点清单

| 知识点 | 说明 |
|--------|------|
| `base64.b64encode(data)` | 把 bytes 编码成 Base64 bytes |
| `base64.b64decode(data)` | 把 Base64 解码回 bytes |
| `.encode("utf-8")` | 字符串转 bytes |
| `.decode("ascii")` | Base64 bytes 转展示字符串 |
| `urlsafe_b64encode()` | URL-safe Base64 编码 |
| padding `=` | 用于补齐 Base64 长度 |
| `validate=True` | 严格校验 Base64 输入 |
| 编码膨胀 | Base64 体积通常增加约三分之一 |

## ➡️ 下一关

下一关：[hashlib](../54-hashlib/README.md)。
