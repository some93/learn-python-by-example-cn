# 第 54 关：hashlib（师兄带你学 Python）

## 🎯 这一关你会学到

- 理解哈希算法的概念
- 使用 MD5、SHA-1、SHA-256
- 实现安全的密码存储（加盐哈希）
- 了解文件校验的应用

## 🤔 先想一个问题

你要存储用户密码，不能存明文（数据库泄露就完了）。但加密后还得能验证密码对不对。这种「只能正向计算、不能反向推导」的技术就是**哈希**。

带着这个问题，我们来看代码。

## 📖 看代码

```python
# hashlib

import hashlib

# MD5（128位，不再安全，仅用于校验）
md5 = hashlib.md5()
md5.update('hello world'.encode('utf-8'))
print(f"MD5: {md5.hexdigest()}")

# 分多次 update 效果相同
md5_2 = hashlib.md5()
md5_2.update('hello '.encode('utf-8'))
md5_2.update('world'.encode('utf-8'))
print(f"MD5: {md5_2.hexdigest()}")    # 和上面一样

# SHA-1（160位）
sha1 = hashlib.sha1('hello world'.encode('utf-8'))
print(f"SHA1: {sha1.hexdigest()}")

# SHA-256（256位，推荐）
sha256 = hashlib.sha256('hello world'.encode('utf-8'))
print(f"SHA256: {sha256.hexdigest()}")

# 用途一：校验文件完整性
def file_hash(path):
    sha = hashlib.sha256()
    with open(path, 'rb') as f:
        while chunk := f.read(8192):
            sha.update(chunk)
    return sha.hexdigest()

# 用途二：存储密码（一定要加盐！）
import secrets

def hash_password(password):
    salt = secrets.token_hex(16)
    hashed = hashlib.sha256((salt + password).encode()).hexdigest()
    return f"{salt}:{hashed}"

def verify_password(password, stored):
    salt, hashed = stored.split(':')
    return hashlib.sha256((salt + password).encode()).hexdigest() == hashed

stored = hash_password('mypassword')
print(f"存储: {stored}")
print(f"验证正确密码: {verify_password('mypassword', stored)}")
print(f"验证错误密码: {verify_password('wrong', stored)}")

# 注意：实际项目中用 bcrypt 或 argon2，比 sha256 更安全
```

## 🔍 师兄给你逐行拆

> 代码已经在注释中做了详细说明，这里挑重点讲。

### 核心要点

- MD5 已不安全，新项目用 SHA-256
- 存密码一定要加盐（salt），防止彩虹表攻击
- 实际项目中用 `bcrypt` 或 `argon2`，比 SHA-256 更适合密码存储
- 哈希是不可逆的：知道哈希值无法推出原始数据
- 大文件用 `update()` 分块计算，不用一次读入内存

## 🏃 跑一下试试

```bash
cd 54-hashlib
python hashlib_demo.py
```

## 💡 师兄的碎碎念

- MD5 已不安全，新项目用 SHA-256
- 存密码一定要加盐（salt），防止彩虹表攻击
- 实际项目中用 `bcrypt` 或 `argon2`，比 SHA-256 更适合密码存储
- 哈希是不可逆的：知道哈希值无法推出原始数据
- 大文件用 `update()` 分块计算，不用一次读入内存

## 🎓 这一关的知识点清单

| 知识点 | 说明 |
|--------|------|
| `hashlib.md5(data)` | 计算 MD5 哈希 |
| `hashlib.sha256(data)` | 计算 SHA-256 哈希 |
| `h.hexdigest()` | 获取十六进制哈希值 |
| `h.update(data)` | 分块更新哈希 |
| `加盐哈希` | salt + password 一起哈希，防彩虹表 |

## ➡️ 下一关

下一关我们学习 [itertools](../55-itertools/README.md)，继续加油！
