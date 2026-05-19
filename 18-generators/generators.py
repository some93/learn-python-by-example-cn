# 生成器（Generator）

# 把列表生成式的 [] 换成 () 就是生成器
g = (x * x for x in range(5))
print(g)           # <generator object ...>
print(next(g))     # 0
print(next(g))     # 1

# 用 for 遍历生成器（推荐方式）
g2 = (x * x for x in range(5))
for val in g2:
    print(val, end=" ")
print()

# 用 yield 关键字定义生成器函数
def fib(max_count):
    n, a, b = 0, 0, 1
    while n < max_count:
        yield b          # yield 暂停并返回值
        a, b = b, a + b
        n += 1

# 调用生成器函数得到生成器对象
for num in fib(10):
    print(num, end=" ")
print()

# 生成器可以节省内存
# list(range(1000000)) 会立刻占用大量内存
# range(1000000) 是惰性的，几乎不占内存

# yield 的执行流程演示
def count_up_to(n):
    print("开始生成")
    i = 1
    while i <= n:
        print(f"  即将 yield {i}")
        yield i
        print(f"  yield {i} 之后继续")
        i += 1
    print("生成结束")

for val in count_up_to(3):
    print(f"收到: {val}")
