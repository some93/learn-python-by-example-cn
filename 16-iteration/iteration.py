# 迭代

from collections.abc import Iterable


print("=== 遍历列表 ===")

students = ["小王", "小李", "小张"]

for student in students:
    print(student)


print("\n=== 遍历字典 ===")

scores = {"小王": 85, "小李": 92, "小张": 78}

# 直接遍历 dict，拿到的是 key
for name in scores:
    print(f"{name}: {scores[name]}")

# 只遍历 value
for score in scores.values():
    print(score)

# 同时遍历 key 和 value
for name, score in scores.items():
    print(f"{name} => {score}")


print("\n=== 遍历字符串 ===")

for ch in "Python":
    print(ch, end=" ")
print()


print("\n=== enumerate：同时拿下标和值 ===")

tasks = ["打开电脑", "写代码", "提交作业"]

for index, task in enumerate(tasks):
    print(f"{index}: {task}")

for step, task in enumerate(tasks, start=1):
    print(f"第 {step} 步：{task}")


print("\n=== zip：并行遍历 ===")

names = ["Alice", "Bob", "Charlie"]
math_scores = [85, 92, 78]
english_scores = [88, 90]

for name, score in zip(names, math_scores):
    print(f"{name}: {score}")

# zip 遇到最短的序列就停止，Charlie 没有英语成绩，所以不会输出
for name, score in zip(names, english_scores):
    print(f"{name} English: {score}")


print("\n=== 判断是否可迭代 ===")

print(isinstance("hello", Iterable))
print(isinstance(123, Iterable))
print(isinstance([1, 2], Iterable))
print(isinstance({"a": 1}, Iterable))
