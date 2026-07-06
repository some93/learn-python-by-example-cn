import re


print("=== match / search / fullmatch ===")
# match 从字符串开头找，开头不是数字，所以失败。
print(bool(re.match(r"\d+", "abc123")))

# search 会扫描整个字符串，能找到中间的数字。
print(re.search(r"\d+", "abc123").group())

# fullmatch 要求整个字符串都符合模式。
print(bool(re.fullmatch(r"\d{3}-\d{4}", "010-1234")))


print("\n=== 提取手机号和邮箱 ===")
text = "联系人: Alice <alice@example.com>, Bob <bob@python.org>; 电话: 13800138000 / 010-12345678"

# (?<!\d) 和 (?!\d) 是前后断言，避免匹配到更长数字串的一部分。
phone_re = re.compile(r"(?<!\d)1[3-9]\d{9}(?!\d)")

# 这个邮箱规则是教学用的简化版，真实业务里不要自己手写复杂邮箱校验。
email_re = re.compile(r"[\w.+-]+@[\w-]+(?:\.[\w-]+)+")

print(phone_re.findall(text))
print(email_re.findall(text))


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
print(match.groupdict())


print("\n=== 贪婪和非贪婪 ===")
html = "<title>Python</title><title>Regex</title>"

# .* 是贪婪匹配，会尽量多吃字符。
print(re.findall(r"<title>.*</title>", html))

# .*? 是非贪婪匹配，遇到第一个 </title> 就停。
print(re.findall(r"<title>.*?</title>", html))


print("\n=== split / sub ===")
# 用多个分隔符切分文本：空白、逗号、分号都算分隔符。
print(re.split(r"[\s,;]+", "python, regex;; tutorial  demo"))

# 替换时可以用 \1、\2 引用前面捕获到的分组。
print(re.sub(r"(\d{3})\d{4}(\d{4})", r"\1****\2", "13800138000"))


print("\n=== flags ===")
config = "HOST=localhost\nPORT=8000\nDEBUG=true"

# re.M 让 ^ 和 $ 按“每一行”的开头结尾匹配。
print(re.findall(r"^\w+", config, flags=re.M))

# re.I 忽略大小写，debug 也能匹配 DEBUG。
print(re.findall(r"debug=(true|false)", config, flags=re.I))
