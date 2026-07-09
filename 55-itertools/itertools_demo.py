# itertools 迭代器工具

import itertools
import operator


print("=== 无限迭代器要截断 ===")

# count 会无限计数，必须配合 islice 或 break 使用。
print(list(itertools.islice(itertools.count(10, 2), 5)))  # [10, 12, 14, 16, 18]

# cycle 会无限循环一个序列。
print(list(itertools.islice(itertools.cycle("ABC"), 8)))  # ['A', 'B', 'C', 'A', 'B', 'C', 'A', 'B']

# repeat 可以重复同一个值；第二个参数限制次数。
print(list(itertools.repeat("Hi", 3)))  # ['Hi', 'Hi', 'Hi']


print("\n=== chain 串联多个可迭代对象 ===")

print(list(itertools.chain("AB", "CD", "EF")))  # ['A', 'B', 'C', 'D', 'E', 'F']

groups = [["Alice", "Bob"], ["Charlie"], ["Diana", "Eric"]]

# chain.from_iterable 适合把“列表的列表”压平成一层。
print(list(itertools.chain.from_iterable(groups)))  # ['Alice', 'Bob', 'Charlie', 'Diana', 'Eric']


print("\n=== groupby 相邻分组 ===")

records = [
    {"class": "二班", "name": "Bob"},
    {"class": "一班", "name": "Alice"},
    {"class": "一班", "name": "Charlie"},
    {"class": "二班", "name": "Diana"},
]

# groupby 只合并相邻元素，所以通常要先按同一个 key 排序。
records.sort(key=lambda item: item["class"])
for class_name, group in itertools.groupby(records, key=lambda item: item["class"]):  # 一班 ['Alice', 'Charlie'] / 二班 ['Bob', 'Diana']
    print(class_name, [item["name"] for item in group])


print("\n=== 排列组合 ===")

# product 是笛卡尔积，等价于多层 for 循环。
print(list(itertools.product("AB", "12")))  # [('A', '1'), ('A', '2'), ('B', '1'), ('B', '2')]

# permutations 是排列，顺序不同算不同结果。
print(list(itertools.permutations("ABC", 2)))  # [('A', 'B'), ('A', 'C'), ('B', 'A'), ('B', 'C'), ('C', 'A'), ('C', 'B')]

# combinations 是组合，顺序不同不重复计算。
print(list(itertools.combinations("ABC", 2)))  # [('A', 'B'), ('A', 'C'), ('B', 'C')]


print("\n=== accumulate 累积计算 ===")

sales = [100, -20, 50, -10]

# 默认做累加，也可以传入 operator.mul、max 等函数。
print(list(itertools.accumulate(sales)))  # [100, 80, 130, 120]
print(list(itertools.accumulate([3, 1, 4, 2], max)))  # [3, 3, 4, 4]
print(list(itertools.accumulate([1, 2, 3, 4], operator.mul)))  # [1, 2, 6, 24]


print("\n=== takewhile / dropwhile ===")

numbers = [1, 3, 5, 8, 9, 2]

# takewhile 遇到第一个不满足条件的元素就停止。
print(list(itertools.takewhile(lambda n: n < 8, numbers)))  # [1, 3, 5]

# dropwhile 跳过开头满足条件的元素，之后全部保留。
print(list(itertools.dropwhile(lambda n: n < 8, numbers)))  # [8, 9, 2]


print("\n=== compress / zip_longest / pairwise ===")

names = ["Alice", "Bob", "Charlie", "Diana"]
selected = [True, False, True, False]

# compress 用布尔选择器过滤数据。
print(list(itertools.compress(names, selected)))  # ['Alice', 'Charlie']

# zip_longest 会按最长序列对齐，缺失位置用 fillvalue 补。
print(list(itertools.zip_longest("ABC", [1, 2], fillvalue="-")))  # [('A', 1), ('B', 2), ('C', '-')]

# pairwise 适合计算相邻元素关系。
temperatures = [21, 23, 22, 25]
print(list(itertools.pairwise(temperatures)))  # [(21, 23), (23, 22), (22, 25)]
print([b - a for a, b in itertools.pairwise(temperatures)])  # [2, -1, 3]
