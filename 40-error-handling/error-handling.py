# 错误处理

import logging
import sys


logging.basicConfig(level=logging.ERROR, format="%(levelname)s:%(message)s", stream=sys.stdout)


print("=== try / except / finally ===")

try:
    print("try...")
    # 这里故意制造除零错误，演示 except 如何接住异常。
    result = 10 / 0
    print("结果:", result)
except ZeroDivisionError as error:
    print("except:", error)  # except: division by zero
finally:
    # finally 不管有没有异常都会执行，常用于释放资源。
    print("finally...")  # finally...


print("\n=== 捕获多种异常 ===")

try:
    # int("abc") 会先抛出 ValueError，后面的除法不会执行。
    result = 10 / int("abc")
except ValueError as error:
    print("ValueError:", error)  # ValueError: invalid literal for int() with base 10: 'abc'
except ZeroDivisionError as error:
    print("ZeroDivisionError:", error)


print("\n=== else：没有异常时执行 ===")

try:
    result = 10 / 2
except ZeroDivisionError:
    print("除零错误")
else:
    # else 只在 try 没有异常时执行。
    print("没有异常，结果:", result)  # 没有异常，结果: 5.0
finally:
    print("清理资源")  # 清理资源


print("\n=== 异常继承关系 ===")

try:
    10 / 0
except Exception as error:
    # Exception 能捕获大多数业务异常，但不要无脑吞掉错误。
    print(type(error).__name__)  # ZeroDivisionError


print("\n=== logging 记录异常 ===")

try:
    int("not-a-number")
except ValueError as error:
    # logging 可以记录错误信息，比 print 更适合真实项目。
    logging.error("转换失败: %s", error)


print("\n=== 主动抛出异常 ===")


def check_age(age):
    if age < 0:
        # 主动抛异常可以把非法输入挡在函数入口。
        raise ValueError(f"年龄不能为负数: {age}")
    return age


try:
    check_age(-1)
except ValueError as error:
    print("捕获:", error)  # 捕获: 年龄不能为负数: -1


print("\n=== 自定义异常 ===")


class AgeError(ValueError):
    # 自定义异常可以让调用方更精确地捕获业务错误。
    pass



def check_adult(age):
    if age < 18:
        raise AgeError("未成年人不能注册")
    return True


try:
    check_adult(16)
except AgeError as error:
    print("AgeError:", error)  # AgeError: 未成年人不能注册


print("\n=== 异常链 raise from ===")

try:
    try:
        1 / 0
    except ZeroDivisionError as error:
        # raise from 会保留原始异常，方便定位根因。
        raise RuntimeError("计算失败") from error
except RuntimeError as error:
    print(error)  # 计算失败
    print(type(error.__cause__).__name__)  # ZeroDivisionError


print("\n=== 重新抛出异常 ===")

try:
    try:
        check_age(-5)
    except ValueError:
        print("记录后继续抛出")  # 记录后继续抛出
        # 单独写 raise 表示重新抛出当前异常。
        raise
except ValueError as error:
    print("外层捕获:", error)  # 外层捕获: 年龄不能为负数: -5
