# 第 4 关：列表 List（师兄带你学 Python）

## 🎯 这一关你会学到

- 列表（list）的创建、索引、修改
- 正索引和负索引
- `append()`、`insert()`、`pop()` 三大操作方法
- 列表可以混装不同类型，以及嵌套列表

## 🤔 先想一个问题

你家书架上有一排书，从左到右整齐排列。你可以说「拿第 3 本」（正向数），也可以说「拿倒数第 1 本」（反向数）。你可以在末尾加一本新书，也可以在中间插一本，还可以抽走任意一本。这就是 Python 的列表——**有序、可变、随机访问**。

和 Go 的数组/切片不同，Python 的列表**可以混装不同类型的元素**——一个列表里同时放字符串、数字、布尔值、甚至另一个列表，完全没问题。

## 📖 看代码

```python
# 创建列表
classmates = ['Michael', 'Bob', 'Tracy']
print(classmates)         # ['Michael', 'Bob', 'Tracy']
print(len(classmates))    # 3

# 索引访问：正索引从 0 开始，负索引从 -1 开始
print(classmates[0])      # Michael
print(classmates[-1])     # Tracy

# 追加、插入、删除
classmates.append('Adam')
classmates.insert(1, 'Jack')
print(classmates)         # ['Michael', 'Jack', 'Bob', 'Tracy', 'Adam']
classmates.pop()          # 删除末尾
classmates.pop(1)         # 删除指定位置
print(classmates)         # ['Michael', 'Bob', 'Tracy']

# 替换元素
classmates[1] = 'Sarah'
print(classmates)         # ['Michael', 'Sarah', 'Tracy']

# 混装不同类型
mixed = ['Apple', 123, True, None, [1, 2, 3]]
print(mixed)              # ['Apple', 123, True, None, [1, 2, 3]]

# 嵌套列表（二维列表）
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(matrix[1][2])    # 6

# 排序和查找
nums = [3, 1, 4, 1, 5, 9]
nums.sort()
print(nums)            # [1, 1, 3, 4, 5, 9]
print(3 in nums)       # True
```

## 🔍 师兄给你逐行拆

### 创建和索引 —— 正着数、倒着数都行

```python
classmates = ['Michael', 'Bob', 'Tracy']
print(classmates[0])      # Michael
print(classmates[-1])     # Tracy
```

**这行在干嘛？**

用方括号 `[]` 创建列表，元素用逗号分隔。索引从 `0` 开始（第一个元素），`-1` 是最后一个，`-2` 是倒数第二个。

**容易踩的坑**

越界访问会报 `IndexError`：`classmates[3]` 在只有 3 个元素的列表里是不合法的（合法范围 0-2）。这和 Go 切片的越界 panic 是一样的道理。

---

### `append()`/`insert()`/`pop()` —— 增删三剑客

```python
classmates.append('Adam')       # 末尾追加
classmates.insert(1, 'Jack')    # 在索引1处插入
classmates.pop()                # 删除末尾
classmates.pop(1)               # 删除索引1处
```

**生活类比**

`append` 像排队时从**队尾**加人，`insert` 像在**队伍中间**插队（后面的人都要往后挪），`pop` 像从队伍里**叫走一个人**（默认叫走最后一个，也可以指定位置）。

---

### 混装类型 —— Python 的自由

```python
mixed = ['Apple', 123, True, None, [1, 2, 3]]
```

**为什么 Python 列表能混装？**

因为 Python 列表存的是**引用（指针）**，不是值本身。每个引用可以指向任意类型的对象。Go 的切片 `[]int` 只能放 `int`，因为 Go 在编译时就要确定内存布局。Python 在运行时动态决定，所以灵活但慢。

## 🏃 跑一下试试

```bash
$ python lists.py
['Michael', 'Bob', 'Tracy']
3
Michael
Tracy
['Michael', 'Jack', 'Bob', 'Tracy', 'Adam']
['Michael', 'Bob', 'Tracy']
['Michael', 'Sarah', 'Tracy']
['Apple', 123, True, None, [1, 2, 3]]
6
[1, 1, 3, 4, 5, 9]
True
```

## 💡 师兄的碎碎念

- `sort()` 是**原地排序**（修改原列表，返回 None），`sorted()` 是**返回新列表**（原列表不变）。新手经常写 `new_list = my_list.sort()` 然后发现 `new_list` 是 `None`。
- 列表拼接用 `+`：`[1, 2] + [3, 4]` 得到 `[1, 2, 3, 4]`。重复用 `*`：`[0] * 5` 得到 `[0, 0, 0, 0, 0]`。
- `remove(value)` 按值删除第一个匹配项：`nums.remove(1)` 删掉第一个 `1`。
- 列表的切片操作（`L[1:3]`）会在第 15 关详细讲，这里先知道有这个东西就行。

## 🎓 这一关的知识点清单

- **创建**：`[elem1, elem2, ...]`，空列表 `[]`。
- **索引**：`L[0]` 正索引，`L[-1]` 负索引。越界报 `IndexError`。
- **增**：`append()` 末尾追加，`insert(i, elem)` 指定位置插入。
- **删**：`pop()` 删末尾，`pop(i)` 删指定位置，`remove(val)` 按值删。
- **改**：`L[i] = new_val` 直接赋值。
- **查**：`val in L` 判断是否存在，`len(L)` 获取长度。
- **混装**：列表可以包含任意类型的元素，包括其他列表。

## ➡️ 下一关

列表是可变的，但有时候你需要一个「创建后就不能改」的序列——这就是元组（Tuple）👉 [下一关：元组 Tuple →](../05-tuples/)
