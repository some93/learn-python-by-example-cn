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
