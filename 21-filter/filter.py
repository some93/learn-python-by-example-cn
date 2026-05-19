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
