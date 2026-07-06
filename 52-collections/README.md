# 第 52 关：collections（师兄带你学 Python）

## 🎯 这一关你会学到

- 用 `namedtuple` 创建字段有名字的轻量对象
- 用 `deque` 实现高效队列和最近访问记录
- 用 `defaultdict` 简化分组和计数
- 用 `Counter` 做词频统计和增减计数
- 用 `OrderedDict` 处理顺序敏感的字典场景
- 用 `ChainMap` 合并多层配置

## 🤔 先想一个问题

普通 `list`、`dict` 已经很好用，但真实项目里经常会遇到更具体的问题：

- 想让坐标点既轻量，又能用 `.x`、`.y` 访问
- 想在列表头部高效插入和弹出
- 想按班级自动分组，不想每次判断 key 是否存在
- 想统计词频并取前几名
- 想把命令行参数、环境变量、默认配置按优先级合并

这些场景就是 `collections` 模块的主场。

## 📖 看代码

```python
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
```

## 🔍 师兄给你拆开讲

`namedtuple` 适合表示字段固定的小数据，比如坐标、颜色、商品规格。它比普通元组可读，比普通类更轻量。`point._asdict()` 可以把它转成字典，便于调试或序列化。

`deque` 是双端队列。`list.append()` 很快，但 `list.insert(0, value)` 和 `list.pop(0)` 需要移动大量元素；`deque.appendleft()` 和 `deque.popleft()` 更适合队列头部操作。`maxlen` 很适合做“最近 3 条浏览记录”这种固定长度窗口。

`defaultdict` 的核心是默认工厂。`defaultdict(list)` 在 key 不存在时自动创建空列表，适合分组；`defaultdict(int)` 自动从 `0` 开始，适合计数。

`Counter` 是专门的计数器。它能直接统计列表、字符串、迭代器，也支持 `update()` 增加计数、`subtract()` 减少计数、`most_common()` 取排行榜。

Python 3.7 之后普通 `dict` 已经保持插入顺序，但 `OrderedDict` 仍然有用：它比较时顺序敏感，还提供 `move_to_end()`，适合实现简单 LRU 缓存。

`ChainMap` 不会真的合并字典，而是把多个映射串起来查找。命令行参数、环境变量、默认配置这种“多层优先级”场景，用它很自然。

## 🏃 跑一下试试

```bash
cd 52-collections
python collections_demo.py
```

输出：

```text
=== namedtuple：轻量数据对象 ===
Point(x=3, y=4)
3 4
True
{'x': 3, 'y': 4}

=== deque：双端队列 ===
['urgent', 'task-1', 'task-2', 'task-3']
urgent
task-3
['task-1', 'task-2']
['search', 'detail', 'cart']

=== defaultdict：自动创建默认值 ===
{'一班': [('Alice', 92), ('Charlie', 78)], '二班': [('Bob', 85)]}
{'python': 3, 'java': 1, 'go': 1}

=== Counter：专门用来计数 ===
Counter({'apple': 3, 'banana': 2, 'cherry': 1})
[('apple', 3), ('banana', 2)]
Counter({'apple': 3, 'banana': 3, 'cherry': 1, 'durian': 1})
Counter({'banana': 3, 'apple': 2, 'cherry': 1, 'durian': 0})

=== OrderedDict：顺序敏感的字典 ===
False
True
['search', 'detail', 'home']

=== ChainMap：合并多个配置来源 ===
True
127.0.0.1
9000
[{'debug': True}, {'host': '127.0.0.1', 'port': 9000}, {'host': '0.0.0.0', 'port': 8000, 'debug': False}]
```

## 💡 师兄的提醒

`collections` 不是为了炫技，而是为了让数据结构贴近问题本身。看到“计数”先想到 `Counter`，看到“分组”先想到 `defaultdict(list)`，看到“两头频繁进出”先想到 `deque`。

如果你只是普通增删改查，内置 `dict` / `list` 仍然是首选。

## 🎓 这一关的知识点清单

| 知识点 | 说明 |
|--------|------|
| `namedtuple()` | 创建字段有名字的元组类型 |
| `_asdict()` | 把 namedtuple 转成字典 |
| `deque()` | 双端队列，两端操作高效 |
| `deque(maxlen=n)` | 固定长度队列 |
| `defaultdict(list)` | 自动创建列表，适合分组 |
| `defaultdict(int)` | 自动从 0 开始，适合计数 |
| `Counter` | 专用计数器 |
| `most_common(n)` | 取出现次数最多的 n 项 |
| `OrderedDict` | 顺序敏感字典 |
| `move_to_end()` | 调整键的顺序 |
| `ChainMap` | 按优先级串联多个映射 |

## ➡️ 下一关

下一关：[base64](../53-base64/README.md)。
