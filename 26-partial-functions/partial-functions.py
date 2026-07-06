# 偏函数（Partial Function）

from functools import partial


print("=== 进制转换 ===")

# int() 默认按十进制转换字符串
print(int("12345"))  # 12345

# int() 可以通过 base 参数指定进制
print(int("12345", base=8))   # 5349
print(int("12345", base=16))  # 74565

# 经常转二进制时，把 base=2 预先固定住
int2 = partial(int, base=2)

print(int2("1000000"))  # 64
print(int2("1010101"))  # 85

# 关键字参数不是锁死的，调用时传同名参数会覆盖预设值
print(int2("10", base=10))  # 10

# partial 对象会记住原函数、预设的位置参数和关键字参数
print(int2.func)
print(int2.args)
print(int2.keywords)


print("\n=== 固定位置参数 ===")

# 固定位置参数时，新参数会追加到后面
max10 = partial(max, 10)

print(max10(5, 6, 7))     # 等价于 max(10, 5, 6, 7)
print(max10(-1, -2, -3))  # 10 仍然参与比较


print("\n=== 奶茶店常用订单 ===")


def make_milk_tea(customer, size, sugar, ice, topping):
    return f"{customer}: {size}, {sugar}, {ice}, 加{topping}"


# 把常用配置固定下来，只留下顾客名和少量临时修改项
office_order = partial(
    make_milk_tea,
    size="中杯",
    sugar="少糖",
    ice="去冰",
    topping="珍珠",
)

print(office_order("小王"))
print(office_order("小李", ice="正常冰"))
print(office_order("小张", topping="椰果"))


print("\n=== 价格格式化 ===")


def format_price(price, currency="CNY", precision=2):
    return f"{currency} {price:.{precision}f}"


# 为不同业务场景准备专用格式化函数
cny_price = partial(format_price, currency="CNY", precision=2)
jpy_price = partial(format_price, currency="JPY", precision=0)

print(cny_price(19.9))
print(jpy_price(1999.6))

prices = [12, 3.5, 99.99]
formatted_prices = [cny_price(price) for price in prices]
print(formatted_prices)


print("\n=== 手写包装函数 ===")


def int16(s):
    return int(s, base=16)


def strict_int2(s):
    return int(s, base=2)


print(int16("ff"))
print(strict_int2("10"))
