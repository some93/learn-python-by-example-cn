# Python 中条件判断使用 if/elif/else 语句

age = 20

# 单个 if 判断
if age >= 18:
    print("你已经成年了")
    print("可以去网吧了")

# if-else 判断
if age >= 18:
    print("adult")
else:
    print("teenager")

# if-elif-else 多条件判断
if age >= 18:
    print("adult")
elif age >= 6:
    print("teenager")
else:
    print("kid")

# 条件表达式中的真假值
# 非零数值、非空字符串、非空列表都被视为 True
# 0、空字符串 ''、空列表 []、None 都被视为 False
if "hello":
    print("非空字符串是 True")

if 0:
    print("这行不会执行")
else:
    print("0 是 False")

# 逻辑运算符 and / or / not
x = 15
if x > 10 and x < 20:
    print(f"{x} 在 10 到 20 之间")

if not x > 100:
    print(f"{x} 不大于 100")

# 简化写法：链式比较
if 10 < x < 20:
    print("Python 支持链式比较，这是语法糖")

# input() 获取用户输入（注意返回的是字符串！）
# s = input("请输入你的年龄：")
# age = int(s)  # 必须转成整数才能比较
# 上面两行注释掉了，取消注释可以交互体验
