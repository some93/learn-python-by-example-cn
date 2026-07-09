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
