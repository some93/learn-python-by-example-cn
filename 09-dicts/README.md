# 第 9 关：字典 Dict（师兄带你学 Python）

## 🎯 这一关你会学到

- 字典（dict）的创建、增删改查
- 为什么 dict 查找这么快（哈希表原理）
- `get()` 方法避免 `KeyError`
- 遍历字典的多种姿势
- dict 的 key 必须是不可变类型

## 🤔 先想一个问题

想象你手机里的通讯录：输入一个名字，立刻找到电话号码。你不需要从第一个人翻到最后一个——这就是**字典**的威力。dict 底层用的是**哈希表**，查找速度几乎是 O(1)，和数据量无关。Go 里的 `map` 和 Python 的 `dict` 是同一类东西。

## 📖 看代码

```python
# 创建字典
scores = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
print(scores['Michael'])     # 95

# 添加 / 修改
scores['Adam'] = 67
scores['Bob'] = 80
print(scores)

# 判断 key 是否存在
print('Michael' in scores)   # True

# get()：安全获取
print(scores.get('Tom'))          # None
print(scores.get('Tom', -1))     # -1

# 删除
scores.pop('Adam')

# 遍历
for key, value in scores.items():
    print(f"{key} => {value}")

# key 必须是不可变类型
d = {(1, 2): 'tuple_key'}   # tuple 可以
# d = {[1, 2]: 'list_key'}  # TypeError!
```

## 🔍 师兄给你逐行拆

### 创建和访问

```python
scores = {'Michael': 95, 'Bob': 75}
print(scores['Michael'])
```

用花括号 `{}` 创建，`key: value` 格式。通过 `d[key]` 访问值。如果 key 不存在，直接报 `KeyError`。

**和 Go map 的对比**

Go 里访问不存在的 key 会返回零值且不报错（`v, ok := m["key"]`），Python 直接报错。所以 Python 推荐用 `get()` 或先 `in` 判断。

---

### `get()` —— 不怕 key 不存在

```python
scores.get('Tom')          # None
scores.get('Tom', -1)     # -1（自定义默认值）
```

`get(key, default)` 在 key 不存在时返回默认值而不是报错。这是 Python 字典最常用的安全访问方式。

---

### 遍历字典

```python
for key, value in scores.items():
    print(f"{key} => {value}")
```

`.items()` 返回所有键值对。也可以只遍历 key：`for k in d:` 或 `for k in d.keys():`。

## 🏃 跑一下试试

```bash
$ python dicts.py
95
{'Michael': 95, 'Bob': 80, 'Tracy': 85, 'Adam': 67}
True
False
None
-1
{'Michael': 95, 'Bob': 80, 'Tracy': 85}
--- 遍历 ---
Michael: 95
Bob: 80
Tracy: 85
Michael => 95
Bob => 80
Tracy => 85
['Michael', 'Bob', 'Tracy']
[95, 80, 85]
{(1, 2): 'tuple_key'}
```

## 💡 师兄的碎碎念

- dict 查找速度极快（O(1)），但**占内存大**。用空间换时间，这是经典的工程权衡。
- Python 3.7+ 保证 dict **按插入顺序**保留元素。3.6 之前是无序的。
- `setdefault(key, default)` 比 `get` 更进一步：如果 key 不存在，不仅返回 default，还会把 `key: default` 写入 dict。
- 字典推导式：`{k: v for k, v in pairs}` 可以快速构建 dict，后面高级特性会讲。

## 🎓 这一关的知识点清单

- **创建**：`{key: value, ...}`，空字典 `{}`。
- **访问**：`d[key]`（不存在报错）或 `d.get(key, default)`（安全）。
- **增/改**：`d[key] = value`。
- **删**：`d.pop(key)`。
- **判断**：`key in d`。
- **遍历**：`d.items()`（键值对）、`d.keys()`（键）、`d.values()`（值）。
- **key 约束**：key 必须是不可变类型（str、int、tuple 可以，list 不行）。

## ➡️ 下一关

字典搞定了！再来看看集合（Set）——自动去重、支持数学集合运算的好工具 👉 [下一关：集合 Set →](../10-sets/)
