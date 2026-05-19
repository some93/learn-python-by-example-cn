# 第 52 关：collections（师兄带你学 Python）

## 🎯 这一关你会学到

- 用 `namedtuple` 创建有名字的元组
- 用 `deque` 实现高效的双端队列
- 用 `defaultdict` 简化字典操作
- 用 `Counter` 快速统计

## 🤔 先想一个问题

普通字典访问不存在的 key 会报错，每次都要先判断太麻烦。普通列表头部插入是 O(n)，太慢。`collections` 模块提供了一组增强版数据结构，解决这些痛点。

带着这个问题，我们来看代码。

## 📖 看代码

```python
# collections 模块

from collections import namedtuple, deque, defaultdict, OrderedDict, Counter

# namedtuple：给元组里的元素起名字
Point = namedtuple('Point', ['x', 'y'])
p = Point(1, 2)
print(p.x, p.y)        # 1 2
print(isinstance(p, tuple))    # True（它就是元组！）

# 用 namedtuple 表示坐标、颜色等
Color = namedtuple('Color', ['red', 'green', 'blue'])
white = Color(255, 255, 255)
print(white.red)    # 255

# deque：双端队列（高效的头部操作）
dq = deque([1, 2, 3])
dq.appendleft(0)     # 头部插入
dq.append(4)          # 尾部插入
print(dq)             # deque([0, 1, 2, 3, 4])
dq.popleft()          # 头部弹出
print(dq)             # deque([1, 2, 3, 4])

# list 的头部操作是 O(n)，deque 是 O(1)

# defaultdict：带默认值的字典
dd = defaultdict(lambda: 'N/A')
dd['name'] = 'Alice'
print(dd['name'])     # Alice
print(dd['score'])    # N/A（普通 dict 会 KeyError）

# 常见用法：统计分组
words = ['apple', 'banana', 'apple', 'cherry', 'banana', 'apple']
word_count = defaultdict(int)
for w in words:
    word_count[w] += 1
print(dict(word_count))    # {'apple': 3, 'banana': 2, 'cherry': 1}

# Counter：计数器（更简洁的统计）
c = Counter(words)
print(c)                       # Counter({'apple': 3, 'banana': 2, 'cherry': 1})
print(c.most_common(2))        # [('apple', 3), ('banana', 2)]

# Counter 也能统计字符串
print(Counter('programming'))   # Counter({'r': 2, 'g': 2, 'm': 2, ...})

# OrderedDict：记住插入顺序的字典
# Python 3.7+ 普通 dict 也保持插入顺序了
# OrderedDict 的特殊之处：两个 OrderedDict 比较时顺序也参与
od1 = OrderedDict([('a', 1), ('b', 2)])
od2 = OrderedDict([('b', 2), ('a', 1)])
print(od1 == od2)    # False（顺序不同）

d1 = {'a': 1, 'b': 2}
d2 = {'b': 2, 'a': 1}
print(d1 == d2)      # True（普通 dict 不比较顺序）
```

## 🔍 师兄给你逐行拆

> 代码已经在注释中做了详细说明，这里挑重点讲。

### 核心要点

- `namedtuple` 是元组的升级版，可以用 `.name` 代替 `[0]` 访问
- `deque` 头部操作是 O(1)，比 list 快得多
- `defaultdict(int)` 配合计数非常方便，不用先判断 key 是否存在
- `Counter` 一行代码完成统计，`most_common(n)` 取前 n 名
- Python 3.7+ 的普通 dict 也保持插入顺序，OrderedDict 的优势在于比较时考虑顺序

## 🏃 跑一下试试

```bash
cd 52-collections
python collections_demo.py
```

## 💡 师兄的碎碎念

- `namedtuple` 是元组的升级版，可以用 `.name` 代替 `[0]` 访问
- `deque` 头部操作是 O(1)，比 list 快得多
- `defaultdict(int)` 配合计数非常方便，不用先判断 key 是否存在
- `Counter` 一行代码完成统计，`most_common(n)` 取前 n 名
- Python 3.7+ 的普通 dict 也保持插入顺序，OrderedDict 的优势在于比较时考虑顺序

## 🎓 这一关的知识点清单

| 知识点 | 说明 |
|--------|------|
| `namedtuple('Name', fields)` | 创建命名元组 |
| `deque()` | 双端队列，两端操作 O(1) |
| `defaultdict(factory)` | 带默认值的字典 |
| `Counter(iterable)` | 元素计数器 |
| `c.most_common(n)` | 获取前 n 个最常见的元素 |

## ➡️ 下一关

下一关我们学习 [base64](../53-base64/README.md)，继续加油！
