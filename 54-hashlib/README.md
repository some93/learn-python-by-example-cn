# 第 54 关：hashlib

## 🎯 这一关你会学到

- 哈希摘要是什么，和加密有什么区别
- 如何计算 MD5、SHA-1、SHA-256
- 为什么可以分多次 `update()`
- 哈希的雪崩效应是什么
- 如何分块计算文件摘要
- 如何用 PBKDF2 演示密码摘要存储
- 为什么验证摘要要用 `hmac.compare_digest()`

## 🤔 先想一个问题

下载软件时，官网常常给一个 SHA-256 值。你下载完文件后也算一遍，如果两个值一样，就说明文件大概率没被篡改。

这就是哈希的用途之一：**把任意长度的数据，计算成固定长度的摘要**。

但哈希不是加密。加密通常能解密回原文，哈希不能反推原文。密码存储利用的正是这个特点：数据库里不存明文密码，只存密码摘要。

## 📖 看代码

```python
# hashlib 哈希算法

import hashlib
import hmac


print("=== 常见哈希算法 ===")

message = "hello world".encode("utf-8")

# MD5 和 SHA-1 已不适合安全场景，这里只用于认识输出形式。
print(hashlib.md5(message).hexdigest())  # 5eb63bbbe01eeed093cb22bb8f5acdc3
print(hashlib.sha1(message).hexdigest())  # 2aae6c35c94fcfb415dbe95f408b9ce91ee846ed
print(hashlib.sha256(message).hexdigest())  # b94d27b9934d3e08a52e52d7da7dabfac484efe37a5380ee9088f7ace2efcde9


print("\n=== 分多次 update 效果相同 ===")

sha_once = hashlib.sha256(b"hello world").hexdigest()

sha_chunks = hashlib.sha256()
sha_chunks.update(b"hello ")
sha_chunks.update(b"world")

print(sha_once)  # b94d27b9934d3e08a52e52d7da7dabfac484efe37a5380ee9088f7ace2efcde9
print(sha_chunks.hexdigest())  # b94d27b9934d3e08a52e52d7da7dabfac484efe37a5380ee9088f7ace2efcde9
print(sha_once == sha_chunks.hexdigest())  # True


print("\n=== 输入稍变，结果完全不同 ===")

# 哈希算法有雪崩效应：输入改 1 个字符，摘要也会大幅变化。
left = hashlib.sha256(b"hello world").hexdigest()
right = hashlib.sha256(b"hello worle").hexdigest()

print(left[:16])  # b94d27b9934d3e08
print(right[:16])  # 0fc30e735a0228a3
print(left == right)  # False


print("\n=== 分块计算文件摘要 ===")

chunks = [b"line 1\n", b"line 2\n", b"line 3\n"]
file_hash = hashlib.sha256()

# 大文件不要一次性读入内存，应该分块 update。
for chunk in chunks:
    file_hash.update(chunk)

print(file_hash.hexdigest())  # 6ca9d5edb68deaadc1d3130c5fc3ec36e12db72ad54e93edcd63bdfb40a83300


print("\n=== PBKDF2 存储密码摘要 ===")

password = "mypassword"
salt = bytes.fromhex("00112233445566778899aabbccddeeff")
iterations = 100_000

# PBKDF2 会反复计算很多轮，比单次 sha256 更适合密码存储。
password_hash = hashlib.pbkdf2_hmac(
    "sha256",
    password.encode("utf-8"),
    salt,
    iterations,
)

stored = f"pbkdf2_sha256${iterations}${salt.hex()}${password_hash.hex()}"
print(stored)  # pbkdf2_sha256$100000$00112233445566778899aabbccddeeff$6edfb86d00311fe67b02df5f772af20c0fc07e2af4e0789e1baacfafbf8390ba


def verify_password(password, stored_text):
    algorithm, iterations_text, salt_hex, digest_hex = stored_text.split("$")
    hash_name = algorithm.removeprefix("pbkdf2_")
    iterations = int(iterations_text)
    salt = bytes.fromhex(salt_hex)
    expected = bytes.fromhex(digest_hex)

    actual = hashlib.pbkdf2_hmac(hash_name, password.encode("utf-8"), salt, iterations)

    # compare_digest 用于避免普通字符串比较带来的时序攻击风险。
    return hmac.compare_digest(actual, expected)


print(verify_password("mypassword", stored))  # True
print(verify_password("wrong-password", stored))  # False
```

## 🔍 师兄给你拆开讲

`hexdigest()` 返回十六进制字符串，适合打印、保存、复制。相同输入永远得到相同摘要；输入稍微变化，摘要就会完全不同，这叫雪崩效应。

`update()` 可以多次调用。哈希对象会把每次喂进去的字节连续处理，所以 `update(b"hello ")` 再 `update(b"world")` 和一次性处理 `b"hello world"` 结果相同。

文件校验时不要一次性 `read()` 整个大文件，应该循环读取小块并 `update()`。示例用内存里的 `chunks` 模拟文件分块，真实文件也是同一个思路。

密码存储不能用“单次 SHA-256(password)”这种写法。攻击者可以高速尝试大量密码。PBKDF2 会加盐并重复计算很多轮，显著提高爆破成本。真实项目里还可以使用 `bcrypt`、`argon2` 或 Web 框架自带的密码哈希工具。

`hmac.compare_digest()` 用于安全比较摘要，避免普通比较在极端安全场景下泄露比较进度。

## 🏃 跑一下试试

```bash
cd 54-hashlib
python hashlib_demo.py
```

输出：

```text
=== 常见哈希算法 ===
5eb63bbbe01eeed093cb22bb8f5acdc3
2aae6c35c94fcfb415dbe95f408b9ce91ee846ed
b94d27b9934d3e08a52e52d7da7dabfac484efe37a5380ee9088f7ace2efcde9

=== 分多次 update 效果相同 ===
b94d27b9934d3e08a52e52d7da7dabfac484efe37a5380ee9088f7ace2efcde9
b94d27b9934d3e08a52e52d7da7dabfac484efe37a5380ee9088f7ace2efcde9
True

=== 输入稍变，结果完全不同 ===
b94d27b9934d3e08
0fc30e735a0228a3
False

=== 分块计算文件摘要 ===
6ca9d5edb68deaadc1d3130c5fc3ec36e12db72ad54e93edcd63bdfb40a83300

=== PBKDF2 存储密码摘要 ===
pbkdf2_sha256$100000$00112233445566778899aabbccddeeff$6edfb86d00311fe67b02df5f772af20c0fc07e2af4e0789e1baacfafbf8390ba
True
False
```

## 💡 师兄的提醒

MD5、SHA-1 不要再用于安全场景。它们仍可能出现在非安全用途里，比如快速校验、兼容旧系统，但新项目优先用 SHA-256 或更合适的方案。

示例为了输出稳定使用固定 salt。真实项目必须给每个密码生成随机 salt，并把算法、迭代次数、salt、摘要一起保存。

## 🎓 这一关的知识点清单

| 知识点 | 说明 |
|--------|------|
| `hashlib.md5()` | 计算 MD5 摘要，不适合安全场景 |
| `hashlib.sha1()` | 计算 SHA-1 摘要，不适合安全场景 |
| `hashlib.sha256()` | 计算 SHA-256 摘要 |
| `update()` | 分块喂入数据 |
| `hexdigest()` | 获取十六进制摘要字符串 |
| 雪崩效应 | 输入微小变化，摘要大幅变化 |
| `pbkdf2_hmac()` | 标准库提供的密码派生函数 |
| salt | 每个密码使用的随机盐 |
| `hmac.compare_digest()` | 更安全地比较摘要 |

## ➡️ 下一关

下一关：[itertools](../55-itertools/README.md)。
