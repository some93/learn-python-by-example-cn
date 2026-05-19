# dict 是键值对集合

# 创建字典
scores = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
print(scores)
print(scores['Michael'])     # 95

# 添加 / 修改
scores['Adam'] = 67          # 添加新键值对
scores['Bob'] = 80           # 修改已有的
print(scores)

# 判断 key 是否存在
print('Michael' in scores)   # True
print('Tom' in scores)       # False

# get() 方法：key 不存在时返回默认值，不报错
print(scores.get('Tom'))          # None
print(scores.get('Tom', -1))     # -1

# 删除 key
scores.pop('Adam')
print(scores)

# 遍历字典
print("--- 遍历 ---")
for key in scores:
    print(f"{key}: {scores[key]}")

# 同时遍历 key 和 value
for key, value in scores.items():
    print(f"{key} => {value}")

# 获取所有 key 和 value
print(list(scores.keys()))
print(list(scores.values()))

# dict 的 key 必须是不可变类型
# d = {[1, 2]: 'list_key'}  # TypeError: unhashable type: 'list'
d = {(1, 2): 'tuple_key'}   # tuple 可以作为 key
print(d)
