# itertools 迭代器工具

import itertools
import operator


print("=== 无限迭代器要截断 ===")

# count 会无限计数，必须配合 islice 或 break 使用。
print(list(itertools.islice(itertools.count(10, 2), 5)))

# cycle 会无限循环一个序列。
print(list(itertools.islice(itertools.cycle("ABC"), 8)))

# repeat 可以重复同一个值；第二个参数限制次数。
print(list(itertools.repeat("Hi", 3)))


print("\n=== chain 串联多个可迭代对象 ===")

print(list(itertools.chain("AB", "CD", "EF")))

groups = [["Alice", "Bob"], ["Charlie"], ["Diana", "Eric"]]

# chain.from_iterable 适合把“列表的列表”压平成一层。
print(list(itertools.chain.from_iterable(groups)))


print("\n=== groupby 相邻分组 ===")

records = [
    {"class": "二班", "name": "Bob"},
    {"class": "一班", "name": "Alice"},
    {"class": "一班", "name": "Charlie"},
    {"class": "二班", "name": "Diana"},
]

# groupby 只合并相邻元素，所以通常要先按同一个 key 排序。
records.sort(key=lambda item: item["class"])
for class_name, group in itertools.groupby(records, key=lambda item: item["class"]):
    print(class_name, [item["name"] for item in group])


print("\n=== 排列组合 ===")

# product 是笛卡尔积，等价于多层 for 循环。
print(list(itertools.product("AB", "12")))

# permutations 是排列，顺序不同算不同结果。
print(list(itertools.permutations("ABC", 2)))

# combinations 是组合，顺序不同不重复计算。
print(list(itertools.combinations("ABC", 2)))


print("\n=== accumulate 累积计算 ===")

sales = [100, -20, 50, -10]

# 默认做累加，也可以传入 operator.mul、max 等函数。
print(list(itertools.accumulate(sales)))
print(list(itertools.accumulate([3, 1, 4, 2], max)))
print(list(itertools.accumulate([1, 2, 3, 4], operator.mul)))


print("\n=== takewhile / dropwhile ===")

numbers = [1, 3, 5, 8, 9, 2]

# takewhile 遇到第一个不满足条件的元素就停止。
print(list(itertools.takewhile(lambda n: n < 8, numbers)))

# dropwhile 跳过开头满足条件的元素，之后全部保留。
print(list(itertools.dropwhile(lambda n: n < 8, numbers)))


print("\n=== compress / zip_longest / pairwise ===")

names = ["Alice", "Bob", "Charlie", "Diana"]
selected = [True, False, True, False]

# compress 用布尔选择器过滤数据。
print(list(itertools.compress(names, selected)))

# zip_longest 会按最长序列对齐，缺失位置用 fillvalue 补。
print(list(itertools.zip_longest("ABC", [1, 2], fillvalue="-")))

# pairwise 适合计算相邻元素关系。
temperatures = [21, 23, 22, 25]
print(list(itertools.pairwise(temperatures)))
print([b - a for a, b in itertools.pairwise(temperatures)])
