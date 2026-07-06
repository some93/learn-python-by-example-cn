# collections 常用数据结构

from collections import ChainMap, Counter, OrderedDict, defaultdict, deque, namedtuple


print("=== namedtuple：轻量数据对象 ===")

# namedtuple 还是元组，但字段有名字，比 p[0] / p[1] 更清楚。
Point = namedtuple("Point", ["x", "y"])
point = Point(3, 4)

print(point)
print(point.x, point.y)
print(isinstance(point, tuple))
print(point._asdict())


print("\n=== deque：双端队列 ===")

# deque 两端 append/pop 都很快，适合队列、栈、最近记录。
queue = deque(["task-1", "task-2"])
queue.append("task-3")
queue.appendleft("urgent")

print(list(queue))
print(queue.popleft())
print(queue.pop())
print(list(queue))

# maxlen 可以固定长度，自动丢掉最旧的数据。
recent_pages = deque(maxlen=3)
for page in ["home", "search", "detail", "cart"]:
    recent_pages.append(page)
print(list(recent_pages))


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

print(dict(students_by_class))

# defaultdict(int) 常用于计数，不需要先判断 key 是否存在。
word_count = defaultdict(int)
for word in ["python", "java", "python", "go", "python"]:
    word_count[word] += 1
print(dict(word_count))


print("\n=== Counter：专门用来计数 ===")

words = ["apple", "banana", "apple", "cherry", "banana", "apple"]
counter = Counter(words)

print(counter)
print(counter.most_common(2))

counter.update(["banana", "durian"])
print(counter)

counter.subtract(["apple", "durian"])
print(counter)


print("\n=== OrderedDict：顺序敏感的字典 ===")

left = OrderedDict([("a", 1), ("b", 2)])
right = OrderedDict([("b", 2), ("a", 1)])

# OrderedDict 比较时会考虑顺序，普通 dict 不会。
print(left == right)
print({"a": 1, "b": 2} == {"b": 2, "a": 1})

cache = OrderedDict()
for key in ["home", "search", "detail"]:
    cache[key] = f"page:{key}"

# move_to_end 可以把刚访问的 key 移到末尾，常用于 LRU 缓存。
cache.move_to_end("home")
print(list(cache.keys()))


print("\n=== ChainMap：合并多个配置来源 ===")

cli_args = {"debug": True}
env_vars = {"host": "127.0.0.1", "port": 9000}
defaults = {"host": "0.0.0.0", "port": 8000, "debug": False}

# ChainMap 查找时从左到右，前面的配置优先级更高。
config = ChainMap(cli_args, env_vars, defaults)

print(config["debug"])
print(config["host"])
print(config["port"])
print(config.maps)
