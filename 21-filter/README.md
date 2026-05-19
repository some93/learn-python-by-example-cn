# 第 21 关：filter（师兄带你学 Python）

## 🎯 这一关你会学到

- filter 过滤序列
- filter() 保留满足条件的元素
- filter 返回惰性 Iterator
- 用 filter 实现素数筛法

## 🤔 先想一个问题

filter 像安检门——每个人都要过一次，合格的放行，不合格的拦截。你只需要定义放行标准（函数），filter 帮你执行筛选。

## 📖 看代码

```python
# filter：过滤序列

# 保留奇数
def is_odd(n):
    return n % 2 == 1

result = filter(is_odd, [1, 2, 3, 4, 5, 6])
print(list(result))    # [1, 3, 5]

# 用 lambda
print(list(filter(lambda x: x % 2 == 1, range(1, 11))))

# 删除空字符串
def not_empty(s):
    return s and s.strip()

result = filter(not_empty, ['A', '', 'B', None, 'C', '  '])
print(list(result))    # ['A', 'B', 'C']

# 用 filter 求素数（埃拉托斯特尼筛法）
def primes():
    yield 2
    it = iter(range(3, 10000, 2))  # 只看奇数
    while True:
        n = next(it)
        yield n
        it = filter(lambda x, n=n: x % n != 0, it)

# 打印前 20 个素数
p = primes()
for _ in range(20):
    print(next(p), end=" ")
print()
```

## 🔍 师兄给你逐行拆

filter 接收一个判断函数和一个序列，把函数依次作用于每个元素，True 的保留，False 的丢弃。

代码中的关键点已经在注释中标注，结合上面的完整代码逐段阅读即可。更多细节请运行代码观察输出。

## 🏃 跑一下试试

```bash
$ python filter.py
```

运行代码，观察输出，对照注释理解每一行。

## 💡 师兄的碎碎念

- **filter(func, iterable)**
- **func 返回 True 保留，False 丢弃**
- **返回 Iterator，需 list() 转换**
- **经典应用：埃拉托斯特尼素数筛**

## 🎓 这一关的知识点清单

- **filter 过滤序列**
- **filter() 保留满足条件的元素**
- **filter 返回惰性 Iterator**
- **用 filter 实现素数筛法**

## ➡️ 下一关

本关搞定！接下来学 sorted 👉 [下一关：sorted →](../22-sorted/)
