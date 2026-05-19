# 第 50 关：正则表达式（师兄带你学 Python）

## 🎯 这一关你会学到

- 掌握正则表达式的基本语法
- 用 `re` 模块进行匹配、分组、替换
- 理解贪婪匹配和非贪婪匹配
- 编译正则表达式提高效率

## 🤔 先想一个问题

你要从一堆文本中找出所有手机号、邮箱地址。一个一个找太慢了，用**正则表达式**写个模式，让程序自动帮你找出来。

带着这个问题，我们来看代码。

## 📖 看代码

```python
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
```

## 🔍 师兄给你逐行拆

> 代码已经在注释中做了详细说明，这里挑重点讲。

### 核心要点

- 正则字符串前面加 `r`（原始字符串），避免反斜杠转义问题
- `re.match()` 从头匹配，`re.search()` 任意位置匹配
- `re.findall()` 找出所有匹配，最常用
- 贪婪匹配 `*` / `+` 会尽量多匹配，加 `?` 变非贪婪
- 用 `re.compile()` 预编译正则，多次使用时效率更高

## 🏃 跑一下试试

```bash
cd 50-regex
python regex.py
```

## 💡 师兄的碎碎念

- 正则字符串前面加 `r`（原始字符串），避免反斜杠转义问题
- `re.match()` 从头匹配，`re.search()` 任意位置匹配
- `re.findall()` 找出所有匹配，最常用
- 贪婪匹配 `*` / `+` 会尽量多匹配，加 `?` 变非贪婪
- 用 `re.compile()` 预编译正则，多次使用时效率更高

## 🎓 这一关的知识点清单

| 知识点 | 说明 |
|--------|------|
| `re.match(pattern, string)` | 从头匹配 |
| `re.findall(pattern, string)` | 找出所有匹配 |
| `re.sub(pattern, repl, string)` | 替换匹配内容 |
| `re.split(pattern, string)` | 用正则切分字符串 |
| `re.compile(pattern)` | 预编译正则表达式 |
| `r'\d+' 原始字符串` | 避免反斜杠转义 |

## ➡️ 下一关

下一关我们学习 [datetime](../51-datetime/README.md)，继续加油！
