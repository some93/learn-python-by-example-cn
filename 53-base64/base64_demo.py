# base64 编码

import base64

# 编码
data = b'Hello, Python!'
encoded = base64.b64encode(data)
print(encoded)    # b'SGVsbG8sIFB5dGhvbiE='

# 解码
decoded = base64.b64decode(encoded)
print(decoded)    # b'Hello, Python!'

# 中文编码
text = '你好世界'.encode('utf-8')
encoded = base64.b64encode(text)
print(encoded)
print(base64.b64decode(encoded).decode('utf-8'))    # 你好世界

# URL 安全的 base64（把 + 和 / 替换为 - 和 _）
url_encoded = base64.urlsafe_b64encode(b'\xfb\xef\xff')
print(url_encoded)    # b'++__' 变成 b'--__'

url_decoded = base64.urlsafe_b64decode(url_encoded)
print(url_decoded)

# base64 的用途
# 1. 邮件附件编码
# 2. 在 URL 中传递二进制数据
# 3. 在 JSON/XML 中嵌入二进制数据
# 4. 简单的数据混淆（注意：不是加密！）

# base64 编码后数据量会增加约 33%
original = b'a' * 100
encoded = base64.b64encode(original)
print(f"原始: {len(original)} 字节, 编码后: {len(encoded)} 字节")
