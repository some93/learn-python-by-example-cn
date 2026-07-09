# 递归函数

# 经典递归：计算阶乘 n!
def fact(n):
    if n == 1:
        return 1
    return n * fact(n - 1)

print(f"5! = {fact(5)}")      # 5! = 120
print(f"10! = {fact(10)}")    # 10! = 3628800

# 递归执行过程：
# fact(5)
# = 5 * fact(4)
# = 5 * 4 * fact(3)
# = 5 * 4 * 3 * fact(2)
# = 5 * 4 * 3 * 2 * fact(1)
# = 5 * 4 * 3 * 2 * 1
# = 120

# 汉诺塔问题
def hanoi(n, source, target, auxiliary):
    if n == 1:
        print(f"{source} -> {target}")
        return
    hanoi(n - 1, source, auxiliary, target)
    print(f"{source} -> {target}")
    hanoi(n - 1, auxiliary, target, source)

print("--- 汉诺塔 (3个盘子) ---")
hanoi(3, 'A', 'C', 'B')  # 依次输出：A -> C / A -> B / C -> B / A -> C / B -> A / B -> C / A -> C

# 栈溢出问题
# fact(1000)  # RecursionError: maximum recursion depth exceeded
# Python 默认递归深度限制是 1000

# 查看和修改递归限制
import sys
print(f"默认递归深度限制: {sys.getrecursionlimit()}")  # 默认递归深度限制: 1000
# sys.setrecursionlimit(10000)  # 可以改，但不建议

# 尾递归写法（Python 不会优化，但了解概念）
def fact_tail(n, acc=1):
    if n == 1:
        return acc
    return fact_tail(n - 1, n * acc)

print(f"5! = {fact_tail(5)}")  # 5! = 120
