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
