# 匿名函数（lambda）


print("=== lambda 基本语法 ===")

# lambda 适合写很短的匿名函数。
square = lambda x: x * x
print(square(5))
print(square.__name__)


def square_def(x):
    # 逻辑稍微复杂一点时，用 def 更清楚，也更方便调试。
    return x * x


print(square_def(5))
print(square_def.__name__)


print("\n=== lambda 用在 sorted 的 key 参数 ===")

students = [
    {"name": "Alice", "score": 85},
    {"name": "Bob", "score": 92},
    {"name": "Charlie", "score": 78},
]

# sorted 的 key 参数常见写法：用 lambda 指定排序依据。
by_score = sorted(students, key=lambda student: student["score"], reverse=True)
print([student["name"] for student in by_score])

pairs = [(1, "one"), (3, "three"), (2, "two")]
# 同一组数据可以按不同字段排序。
print(sorted(pairs, key=lambda pair: pair[0]))
print(sorted(pairs, key=lambda pair: len(pair[1])))


print("\n=== lambda 配合 map/filter ===")

# lambda 经常和高阶函数一起出现，但别为了简短牺牲可读性。
print(list(map(lambda x: x * x, [1, 2, 3, 4, 5])))
print(list(filter(lambda x: x % 2 == 1, range(1, 11))))


print("\n=== lambda 作为返回值 ===")


def make_adder(n):
    # 返回的 lambda 会记住外层的 n，这也是闭包。
    return lambda x: x + n


add5 = make_adder(5)
add10 = make_adder(10)
print(add5(3))
print(add10(3))


print("\n=== 复杂逻辑用 def 更清楚 ===")


def classify_score(score):
    # 多分支逻辑不适合写成 lambda。
    if score >= 90:
        return "优秀"
    if score >= 60:
        return "及格"
    return "不及格"


print(classify_score(95))
print(classify_score(72))
print(classify_score(50))
