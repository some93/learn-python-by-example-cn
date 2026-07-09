# Python 的循环：for 和 while

# for...in 循环：遍历列表
names = ['Michael', 'Bob', 'Tracy']
for name in names:                 # 依次输出：Hello, Michael! / Hello, Bob! / Hello, Tracy!
    print(f"Hello, {name}!")

# range() 生成整数序列
print("--- range ---")
for i in range(5):       # 0, 1, 2, 3, 4
    print(i, end=" ")
print()

for i in range(1, 6):    # 1, 2, 3, 4, 5
    print(i, end=" ")
print()

for i in range(0, 10, 2): # 0, 2, 4, 6, 8（步长为2）
    print(i, end=" ")
print()

# 计算 1+2+...+100
total = 0
for i in range(1, 101):
    total += i
print(f"1+2+...+100 = {total}")  # 1+2+...+100 = 5050

# while 循环
print("--- while ---")
n = 10
while n > 0:                      # 10 9 8 7 6 5 4 3 2 1
    print(n, end=" ")
    n -= 1
print()

# break：提前退出循环
print("--- break ---")
for i in range(10):               # 0 1 2 3 4
    if i == 5:
        break
    print(i, end=" ")
print()

# continue：跳过本次循环
print("--- continue ---")
for i in range(10):               # 1 3 5 7 9
    if i % 2 == 0:
        continue
    print(i, end=" ")   # 只打印奇数
print()

# for...else：循环正常结束（没有被 break）时执行 else
print("--- for...else ---")
for i in range(5):
    if i == 99:   # 不会命中
        break
else:
    print("循环正常结束，没有 break")  # 循环正常结束，没有 break
