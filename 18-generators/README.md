# 第 18 关：生成器（师兄带你学 Python）

## 🎯 这一关你会学到

- 生成器表达式 `(expr for item in iterable)`
- 生成器的惰性求值：需要一个，才算一个
- `next()` 和 `StopIteration`
- `yield` 如何定义生成器函数
- 生成器只能消费一次，以及它为什么省内存

## 🤔 先想一个问题

列表生成式像奶茶店提前把 1000 杯奶茶全做好，整整齐齐摆在桌上。优点是拿起来快，缺点是桌子可能放不下。

生成器像现点现做：顾客要一杯，师傅做一杯；不来顾客，就不做。它不会一次性把所有结果都算出来，而是**边用边生成**。

所以当数据很多、甚至无限多时，生成器就很香。

## 📖 看代码

```python
# 生成器（Generator）


print("=== 列表 vs 生成器表达式 ===")

# 列表会一次性把所有结果算出来并放进内存。
squares_list = [x * x for x in range(5)]

# 生成器表达式只保存计算规则，需要时才产出下一个值。
squares_gen = (x * x for x in range(5))

print(squares_list)
print(type(squares_gen).__name__)
# next() 每调用一次，生成器就向前走一步。
print(next(squares_gen))
print(next(squares_gen))
print(list(squares_gen))


print("\n=== 生成器只能消费一次 ===")

numbers = (x for x in range(3))
# 第一次 list() 会把生成器里的值全部取完。
print(list(numbers))
# 第二次再取时，生成器已经空了。
print(list(numbers))


print("\n=== StopIteration ===")

one_item = (x for x in [10])
print(next(one_item))
try:
    # 生成器没有更多值时，会抛出 StopIteration。
    print(next(one_item))
except StopIteration:
    print("生成器已经取完")


print("\n=== yield 定义生成器函数 ===")


def fib(max_count):
    n, a, b = 0, 0, 1
    while n < max_count:
        # yield 会返回一个值，同时暂停函数状态。
        yield b
        a, b = b, a + b
        n += 1


print(list(fib(10)))


print("\n=== yield 的暂停和恢复 ===")


def count_up_to(n):
    print("开始生成")
    i = 1
    while i <= n:
        print(f"  即将 yield {i}")
        # 外层 for 收到这个值后，函数会停在这里。
        yield i
        # 下一次取值时，从 yield 后面继续执行。
        print(f"  yield {i} 之后继续")
        i += 1
    print("生成结束")


for value in count_up_to(3):
    print(f"收到: {value}")
```

## 🔍 师兄给你逐行拆

### `[]` 和 `()` 的差别很大

```python
squares_list = [x * x for x in range(5)]
squares_gen = (x * x for x in range(5))

print(squares_list)
print(type(squares_gen).__name__)
```

**这行在干嘛？**

`[x * x for x in range(5)]` 是列表生成式，会马上算出完整列表：

```python
[0, 1, 4, 9, 16]
```

`(x * x for x in range(5))` 是生成器表达式，不会马上算出所有值，只得到一个生成器对象。

**为什么这么写？**

列表像一次性把饭全端上桌；生成器像叫号取餐，需要一个才做一个。数据量小时区别不大，数据量大时，生成器能明显节省内存。

**容易踩的坑**

不要直接把生成器对象打印出来当教程输出：

```python
print(squares_gen)
```

它会显示类似 `<generator object ... at 0x...>`，里面的地址每次都可能不一样，不适合写成固定运行结果。

---

### `next()` —— 手动向生成器要下一个值

```python
print(next(squares_gen))
print(next(squares_gen))
print(list(squares_gen))
```

**这行在干嘛？**

第一次 `next(squares_gen)` 取出 `0`，第二次取出 `1`。之后再用 `list(squares_gen)`，只能拿到剩下的 `[4, 9, 16]`。

**为什么会这样？**

生成器会记住自己走到哪一步了。取过的值不会倒回去重新给你。

**生活类比**

生成器像排队取号机。你拿了 1 号，再拿就是 2 号，不会又吐一张 1 号。

---

### 生成器只能消费一次

```python
numbers = (x for x in range(3))
print(list(numbers))
print(list(numbers))
```

**这行在干嘛？**

第一次 `list(numbers)` 会把生成器里的 `0, 1, 2` 全取完，所以输出：

```python
[0, 1, 2]
```

第二次再取，生成器已经空了，只能得到：

```python
[]
```

**容易踩的坑**

如果你要反复遍历同一批结果，生成器不合适，应该用列表：

```python
data = list(numbers)
```

但注意：一旦转成列表，就会一次性占用内存。

---

### `StopIteration` —— 取完了就告诉你

```python
one_item = (x for x in [10])
print(next(one_item))
try:
    print(next(one_item))
except StopIteration:
    print("生成器已经取完")
```

**这行在干嘛？**

`one_item` 里面只有一个值 `10`。第一次 `next()` 能拿到 `10`，第二次再拿就没了，于是 Python 抛出 `StopIteration`。

**为什么平时很少看到这个异常？**

因为 `for` 循环会自动处理它：

```python
for x in one_item:
    ...
```

循环内部会不断调用 `next()`，遇到 `StopIteration` 就安静结束，不会把异常直接甩到你脸上。

---

### `yield` —— 暂停函数，而不是结束函数

```python
def fib(max_count):
    n, a, b = 0, 0, 1
    while n < max_count:
        yield b
        a, b = b, a + b
        n += 1
```

**这行在干嘛？**

这是一个生成斐波那契数列的生成器函数。只要函数体里出现 `yield`，调用它时就不会立刻执行函数体，而是返回一个生成器对象。

真正执行发生在你遍历它、或者调用 `next()` 的时候。

**`yield` 和 `return` 有什么区别？**

- `return`：函数结束，把结果一次性还给你。
- `yield`：函数暂停，把当前值还给你，下次还能从暂停处继续执行。

---

### 看清 `yield` 的暂停和恢复

```python
def count_up_to(n):
    print("开始生成")
    i = 1
    while i <= n:
        print(f"  即将 yield {i}")
        yield i
        print(f"  yield {i} 之后继续")
        i += 1
    print("生成结束")
```

**这行在干嘛？**

这个例子故意在 `yield` 前后打印文字，让你看到生成器的执行顺序。

当执行到 `yield i` 时，函数暂停，把 `i` 交给外面的 `for` 循环。下一轮循环继续要值时，函数才会从 `yield i` 的下一行接着跑。

**生活类比**

`yield` 像游戏存档点。你打到这里先暂停，把当前成果交出去；下次继续时，不是从头开始，而是从存档点后面继续。

## 🏃 跑一下试试

```bash
$ python generators.py
=== 列表 vs 生成器表达式 ===
[0, 1, 4, 9, 16]
generator
0
1
[4, 9, 16]

=== 生成器只能消费一次 ===
[0, 1, 2]
[]

=== StopIteration ===
10
生成器已经取完

=== yield 定义生成器函数 ===
[1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

=== yield 的暂停和恢复 ===
开始生成
  即将 yield 1
收到: 1
  yield 1 之后继续
  即将 yield 2
收到: 2
  yield 2 之后继续
  即将 yield 3
收到: 3
  yield 3 之后继续
生成结束
```

## 💡 师兄的碎碎念

- 生成器表达式用圆括号：`(expr for item in iterable)`，列表生成式用方括号：`[expr for item in iterable]`。
- 生成器是惰性的，不会一次性算完所有结果。
- 生成器只能向前消费，不能倒退，也不能自动重新开始。
- `for` 循环内部会自动处理 `StopIteration`，所以遍历生成器时通常不用自己捕获异常。
- 数据量小、需要反复使用时，用列表；数据量大、只遍历一次时，优先考虑生成器。

## 🎓 这一关的知识点清单

- **生成器表达式**：把列表生成式的 `[]` 换成 `()`，得到按需产出值的生成器。
- **惰性求值**：需要下一个值时才计算，节省内存。
- **next()**：手动从生成器里取下一个值。
- **StopIteration**：生成器取完时抛出的异常，`for` 循环会自动处理。
- **yield**：定义生成器函数，暂停函数并返回一个值，下次从暂停处继续。
- **一次性消费**：生成器取完就空了，想重复使用需要重新创建或转成列表。

## ➡️ 下一关

生成器其实是一种迭代器。下一关我们拆开看 `Iterable` 和 `Iterator` 的区别，以及 `for` 循环背后到底做了什么 👉 [下一关：迭代器 →](../19-iterators/)


