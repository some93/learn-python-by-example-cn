# 第 50 关：正则表达式

## 🎯 这一关你会学到

- 用 `re` 模块查找、校验、提取和替换文本
- 区分 `match()`、`search()`、`fullmatch()` 的使用场景
- 使用普通分组、命名分组和 `groupdict()` 提取结构化数据
- 理解贪婪匹配、非贪婪匹配和常用 `flags`
- 知道正则表达式适合什么、不适合什么

## 🤔 先想一个问题

你拿到一段混杂文本，里面有手机号、邮箱、日志行、配置项。人工切字符串当然能做，但规则稍微复杂一点，`split()` 和 `find()` 很快就会变成一堆脆弱的判断。

正则表达式的价值在于：**用一个模式描述文本规则，再让程序按这个规则去匹配**。它特别适合处理“格式明确”的文本，比如手机号、日志、简单配置、文件名、表单字段。

## 📖 看代码

```python
import re


print("=== match / search / fullmatch ===")
# match 从字符串开头找，开头不是数字，所以失败。
print(bool(re.match(r"\d+", "abc123")))  # False

# search 会扫描整个字符串，能找到中间的数字。
print(re.search(r"\d+", "abc123").group())  # 123

# fullmatch 要求整个字符串都符合模式。
print(bool(re.fullmatch(r"\d{3}-\d{4}", "010-1234")))  # True


print("\n=== 提取手机号和邮箱 ===")
text = "联系人: Alice <alice@example.com>, Bob <bob@python.org>; 电话: 13800138000 / 010-12345678"

# (?<!\d) 和 (?!\d) 是前后断言，避免匹配到更长数字串的一部分。
phone_re = re.compile(r"(?<!\d)1[3-9]\d{9}(?!\d)")

# 这个邮箱规则是教学用的简化版，真实业务里不要自己手写复杂邮箱校验。
email_re = re.compile(r"[\w.+-]+@[\w-]+(?:\.[\w-]+)+")

print(phone_re.findall(text))  # ['13800138000']
print(email_re.findall(text))  # ['alice@example.com', 'bob@python.org']


print("\n=== 命名分组解析日志 ===")
line = "2026-07-06 09:30 ERROR payment timeout"

# ?P<name> 可以给分组命名，后面用 groupdict() 直接拿字典。
log_re = re.compile(
    r"(?P<date>\d{4}-\d{2}-\d{2}) "
    r"(?P<time>\d{2}:\d{2}) "
    r"(?P<level>INFO|WARN|ERROR) "
    r"(?P<message>.+)"
)
match = log_re.fullmatch(line)
print(match.groupdict())  # {'date': '2026-07-06', 'time': '09:30', 'level': 'ERROR', 'message': 'payment timeout'}


print("\n=== 贪婪和非贪婪 ===")
html = "<title>Python</title><title>Regex</title>"

# .* 是贪婪匹配，会尽量多吃字符。
print(re.findall(r"<title>.*</title>", html))  # ['<title>Python</title><title>Regex</title>']

# .*? 是非贪婪匹配，遇到第一个 </title> 就停。
print(re.findall(r"<title>.*?</title>", html))  # ['<title>Python</title>', '<title>Regex</title>']


print("\n=== split / sub ===")
# 用多个分隔符切分文本：空白、逗号、分号都算分隔符。
print(re.split(r"[\s,;]+", "python, regex;; tutorial  demo"))  # ['python', 'regex', 'tutorial', 'demo']

# 替换时可以用 \1、\2 引用前面捕获到的分组。
print(re.sub(r"(\d{3})\d{4}(\d{4})", r"\1****\2", "13800138000"))  # 138****8000


print("\n=== flags ===")
config = "HOST=localhost\nPORT=8000\nDEBUG=true"

# re.M 让 ^ 和 $ 按“每一行”的开头结尾匹配。
print(re.findall(r"^\w+", config, flags=re.M))  # ['HOST', 'PORT', 'DEBUG']

# re.I 忽略大小写，debug 也能匹配 DEBUG。
print(re.findall(r"debug=(true|false)", config, flags=re.I))  # ['true']
```

## 🔍 师兄给你拆开讲

`r"\d+"` 前面的 `r` 表示原始字符串。正则里经常出现反斜杠，如果不写 `r`，Python 字符串本身会先处理一遍转义，代码会变得难读，也更容易写错。

`match()`、`search()`、`fullmatch()` 的差别一定要分清：`match()` 只看开头，`search()` 在任意位置找，`fullmatch()` 要求整段文本完全符合规则。做表单校验时通常用 `fullmatch()`，从文章里找内容时通常用 `search()` 或 `findall()`.

`findall()` 会返回所有匹配结果。示例里手机号用到了 `(?<!\d)` 和 `(?!\d)`，它们叫断言，用来限制手机号前后不能再接数字，避免从更长数字串里截出一段假手机号。

命名分组 `(?P<date>...)` 适合解析日志、配置、固定格式文本。匹配成功后，`groupdict()` 会把分组名和值组成字典，这比靠 `group(1)`、`group(2)` 猜位置更清楚。

`.*` 默认是贪婪的，会尽可能多匹配；`.*?` 是非贪婪的，会尽可能少匹配。处理 HTML、引号内容、括号内容时，这个差别很常见。不过真实 HTML 不建议靠正则完整解析，要用专门的 HTML 解析库。

## 🏃 跑一下试试

```bash
cd 50-regex
python regex.py
```

输出：

```text
=== match / search / fullmatch ===
False
123
True

=== 提取手机号和邮箱 ===
['13800138000']
['alice@example.com', 'bob@python.org']

=== 命名分组解析日志 ===
{'date': '2026-07-06', 'time': '09:30', 'level': 'ERROR', 'message': 'payment timeout'}

=== 贪婪和非贪婪 ===
['<title>Python</title><title>Regex</title>']
['<title>Python</title>', '<title>Regex</title>']

=== split / sub ===
['python', 'regex', 'tutorial', 'demo']
138****8000

=== flags ===
['HOST', 'PORT', 'DEBUG']
['true']
```

## 💡 师兄的提醒

正则表达式很强，但别把所有字符串问题都交给它。简单分隔用 `split()`，固定前后缀用 `startswith()` / `endswith()`，复杂 HTML/XML/JSON 用专门解析器。

正则写复杂以后，要把模式拆开命名，优先用 `re.compile()` 复用；关键规则最好配几组正反例测试，避免“看着能跑，其实漏了边界”。

## 🎓 这一关的知识点清单

| 知识点 | 说明 |
|--------|------|
| `r"..."` | 原始字符串，适合书写正则 |
| `re.match()` | 从字符串开头匹配 |
| `re.search()` | 在字符串任意位置搜索 |
| `re.fullmatch()` | 要求整个字符串完全匹配 |
| `re.findall()` | 返回所有匹配结果 |
| `re.sub()` | 替换匹配内容 |
| `re.split()` | 按正则规则切分字符串 |
| `(?P<name>...)` | 命名分组 |
| `groupdict()` | 把命名分组结果转成字典 |
| `re.M` / `re.I` | 多行匹配 / 忽略大小写 |

## ➡️ 下一关

下一关：[datetime](../51-datetime/README.md)。


