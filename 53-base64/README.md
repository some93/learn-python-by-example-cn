# 第 53 关：base64（师兄带你学 Python）

## 🎯 这一关你会学到

- 理解 base64 编码的原理和用途
- 用 `base64` 模块编码和解码
- 了解 URL 安全的 base64 变体

## 🤔 先想一个问题

邮件附件、网页里的小图片、JWT Token……这些地方经常看到一串奇怪的字母数字。其实它们都是 **base64 编码**——把二进制数据变成纯文本的一种方式。

带着这个问题，我们来看代码。

## 📖 看代码

```python
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
```

## 🔍 师兄给你逐行拆

> 代码已经在注释中做了详细说明，这里挑重点讲。

### 核心要点

- base64 不是加密！任何人都能解码，只是一种编码方式
- `b64encode` 接受 `bytes`，返回 `bytes`
- 编码后数据量增加约 33%
- `urlsafe_b64encode` 在 URL 中使用更安全（把 + 和 / 替换掉）
- 常见用途：邮件附件、Data URL、JWT、在文本协议中传二进制数据

## 🏃 跑一下试试

```bash
cd 53-base64
python base64_demo.py
```

## 💡 师兄的碎碎念

- base64 不是加密！任何人都能解码，只是一种编码方式
- `b64encode` 接受 `bytes`，返回 `bytes`
- 编码后数据量增加约 33%
- `urlsafe_b64encode` 在 URL 中使用更安全（把 + 和 / 替换掉）
- 常见用途：邮件附件、Data URL、JWT、在文本协议中传二进制数据

## 🎓 这一关的知识点清单

| 知识点 | 说明 |
|--------|------|
| `base64.b64encode(data)` | 编码为 base64 |
| `base64.b64decode(data)` | 解码 base64 |
| `base64.urlsafe_b64encode` | URL 安全的编码 |
| `编码膨胀` | 编码后体积增加约 33% |

## ➡️ 下一关

下一关我们学习 [hashlib](../54-hashlib/README.md)，继续加油！
