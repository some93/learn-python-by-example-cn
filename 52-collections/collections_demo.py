# collections 常用数据结构

from collections import ChainMap, Counter, OrderedDict, defaultdict, deque, namedtuple


print("=== namedtuple：轻量数据对象 ===")

# namedtuple 还是元组，但字段有名字，比 p[0] / p[1] 更清楚。
Point = namedtuple("Point", ["x", "y"])
point = Point(3, 4)

print(point)  # Point(x=3, y=4)
print(point.x, point.y)  # 3 4
print(isinstance(point, tuple))  # True
print(point._asdict())  # {'x': 3, 'y': 4}


print("\n=== deque：双端队列 ===")

# deque 两端 append/pop 都很快，适合队列、栈、最近记录。
queue = deque(["task-1", "task-2"])
queue.append("task-3")
queue.appendleft("urgent")

print(list(queue))  # ['urgent', 'task-1', 'task-2', 'task-3']
print(queue.popleft())  # urgent
print(queue.pop())  # task-3
print(list(queue))  # ['task-1', 'task-2']

# maxlen 可以固定长度，自动丢掉最旧的数据。
recent_pages = deque(maxlen=3)
for page in ["home", "search", "detail", "cart"]:
    recent_pages.append(page)
print(list(recent_pages))  # ['search', 'detail', 'cart']


print("\n=== defaultdict：自动创建默认值 ===")

scores = [
    ("一班", "Alice", 92),
    ("二班", "Bob", 85),
    ("一班", "Charlie", 78),
]

# defaultdict(list) 常用于按 key 分组。
students_by_class = defaultdict(list)
for class_name, name, score in scores:
    students_by_class[class_name].append((name, score))

print(dict(students_by_class))  # {'一班': [('Alice', 92), ('Charlie', 78)], '二班': [('Bob', 85)]}

# defaultdict(int) 常用于计数，不需要先判断 key 是否存在。
word_count = defaultdict(int)
for word in ["python", "java", "python", "go", "python"]:
    word_count[word] += 1
print(dict(word_count))  # {'python': 3, 'java': 1, 'go': 1}


print("\n=== Counter：专门用来计数 ===")

words = ["apple", "banana", "apple", "cherry", "banana", "apple"]
counter = Counter(words)

print(counter)  # Counter({'apple': 3, 'banana': 2, 'cherry': 1})
print(counter.most_common(2))  # [('apple', 3), ('banana', 2)]

counter.update(["banana", "durian"])
print(counter)  # Counter({'apple': 3, 'banana': 3, 'cherry': 1, 'durian': 1})

counter.subtract(["apple", "durian"])
print(counter)  # Counter({'banana': 3, 'apple': 2, 'cherry': 1, 'durian': 0})


print("\n=== OrderedDict：顺序敏感的字典 ===")

left = OrderedDict([("a", 1), ("b", 2)])
right = OrderedDict([("b", 2), ("a", 1)])

# OrderedDict 比较时会考虑顺序，普通 dict 不会。
print(left == right)  # False
print({"a": 1, "b": 2} == {"b": 2, "a": 1})  # True

cache = OrderedDict()
for key in ["home", "search", "detail"]:
    cache[key] = f"page:{key}"

# move_to_end 可以把刚访问的 key 移到末尾，常用于 LRU 缓存。
cache.move_to_end("home")
print(list(cache.keys()))  # ['search', 'detail', 'home']


print("\n=== ChainMap：合并多个配置来源 ===")

cli_args = {"debug": True}
env_vars = {"host": "127.0.0.1", "port": 9000}
defaults = {"host": "0.0.0.0", "port": 8000, "debug": False}

# ChainMap 查找时从左到右，前面的配置优先级更高。
config = ChainMap(cli_args, env_vars, defaults)

print(config["debug"])  # True
print(config["host"])  # 127.0.0.1
print(config["port"])  # 9000
print(config.maps)  # [{'debug': True}, {'host': '127.0.0.1', 'port': 9000}, {'host': '0.0.0.0', 'port': 8000, 'debug': False}]
