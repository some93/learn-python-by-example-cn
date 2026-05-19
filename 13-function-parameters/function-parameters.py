# 函数的参数

# 1. 位置参数（最普通的参数）
def power(x, n):
    return x ** n

print(power(2, 10))    # 1024

# 2. 默认参数
def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}!")

greet("Alice")                # Hello, Alice!
greet("Bob", "Hi")           # Hi, Bob!

# ⚠️ 默认参数的陷阱：默认值必须是不可变对象！
def bad_append(item, lst=[]):   # ❌ 危险！
    lst.append(item)
    return lst

print(bad_append(1))    # [1]
print(bad_append(2))    # [1, 2] —— 不是 [2]！默认 list 被共享了！

def good_append(item, lst=None):  # ✅ 正确写法
    if lst is None:
        lst = []
    lst.append(item)
    return lst

print(good_append(1))   # [1]
print(good_append(2))   # [2]

# 3. 可变参数 *args
def calc_sum(*numbers):
    total = 0
    for n in numbers:
        total += n
    return total

print(calc_sum(1, 2, 3))         # 6
print(calc_sum(1, 2, 3, 4, 5))   # 15

# 把列表传给可变参数
nums = [1, 2, 3, 4]
print(calc_sum(*nums))            # 10（用 * 解包）

# 4. 关键字参数 **kwargs
def person(name, age, **kwargs):
    print(f"name: {name}, age: {age}, other: {kwargs}")

person("Alice", 25)
person("Bob", 30, city="Beijing", job="Engineer")

# 5. 命名关键字参数（*, 后面的参数必须用名字传）
def person2(name, age, *, city, job):
    print(f"{name}, {age}, {city}, {job}")

person2("Charlie", 35, city="Shanghai", job="Teacher")
# person2("Charlie", 35, "Shanghai", "Teacher")  # TypeError!

# 参数组合顺序：位置参数 → 默认参数 → *args → 命名关键字 → **kwargs
def f(a, b=0, *args, keyword_only, **kwargs):
    print(f"a={a}, b={b}, args={args}, keyword_only={keyword_only}, kwargs={kwargs}")

f(1, 2, 3, 4, keyword_only="yes", extra="data")
