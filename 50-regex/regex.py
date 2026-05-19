# 正则表达式

import re

# 基础匹配
print(re.match(r'\d{3}-\d{4}', '010-1234'))    # 匹配成功

# 常用元字符
# \d 数字    \w 字母/数字/下划线    \s 空白字符
# .  任意字符   * 0或多个   + 1或多个   ? 0或1个
# {n} 恰好n个   {n,m} n到m个

# 匹配手机号
pattern = r'^1[3-9]\d{9}$'
print(re.match(pattern, '13800138000'))    # 匹配
print(re.match(pattern, '12345678901'))    # None

# 匹配邮箱（简化版）
email_pattern = r'^[\w.+-]+@[\w-]+\.[\w.]+$'
print(re.match(email_pattern, 'user@example.com'))    # 匹配

# 分组提取
m = re.match(r'^(\d{3})-(\d{3,8})$', '010-12345')
if m:
    print(m.group(0))    # 010-12345（整个匹配）
    print(m.group(1))    # 010（第一组）
    print(m.group(2))    # 12345（第二组）

# 贪婪 vs 非贪婪
print(re.match(r'^(\d+)(0*)$', '102300').groups())
# ('102300', '') —— \d+ 贪婪，吃掉了所有数字

print(re.match(r'^(\d+?)(0*)$', '102300').groups())
# ('1023', '00') —— \d+? 非贪婪，尽量少匹配

# 切分字符串
print(re.split(r'[\s,;]+', 'a,b;; c  d'))    # ['a', 'b', 'c', 'd']

# 编译正则（提高效率）
phone_re = re.compile(r'^1[3-9]\d{9}$')
print(phone_re.match('13912345678'))

# 替换
print(re.sub(r'\d+', '#', 'abc123def456'))    # abc#def#

# findall：找出所有匹配
print(re.findall(r'\d+', 'age=18, score=99'))    # ['18', '99']
