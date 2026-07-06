# filter：过滤序列


print("=== filter 基本用法 ===")


def is_odd(n):
    return n % 2 == 1


# filter 返回惰性迭代器，只保留函数返回真值的元素。
result = filter(is_odd, [1, 2, 3, 4, 5, 6])
print(type(result).__name__)
print(list(result))
# filter 结果消费完之后不能重复使用。
print(list(result))


print("\n=== filter 和列表生成式对比 ===")

numbers = range(1, 11)
# 简单过滤时，列表生成式通常更容易读。
print(list(filter(is_odd, numbers)))
print([n for n in range(1, 11) if is_odd(n)])


print("\n=== filter(None, iterable) ===")

mixed = [0, 1, "", "Python", [], [1], None, True, False]
# 函数传 None 时，会自动过滤掉所有假值。
print(list(filter(None, mixed)))


print("\n=== 删除空字符串 ===")


def not_empty(text):
    # text and ... 可以避免 None 调用 strip() 报错。
    return text and text.strip()


items = ["A", "", "B", None, "C", "  "]
print(list(filter(not_empty, items)))


print("\n=== 用 filter 求素数 ===")


def odd_numbers():
    n = 1
    while True:
        n += 2
        # 素数里除了 2 都是奇数，所以只生成奇数候选。
        yield n


def not_divisible(n):
    # 返回一个过滤函数：剔除能被 n 整除的数。
    return lambda x: x % n != 0


def primes():
    yield 2
    it = odd_numbers()
    while True:
        n = next(it)
        yield n
        # 每发现一个素数，就用它过滤后面的候选数。
        it = filter(not_divisible(n), it)


p = primes()
first_primes = [next(p) for _ in range(20)]
print(first_primes)
