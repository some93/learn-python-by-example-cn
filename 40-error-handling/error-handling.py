# 错误处理

# try...except...finally
try:
    print("try...")
    r = 10 / 0
    print("结果:", r)       # 不会执行
except ZeroDivisionError as e:
    print("except:", e)
finally:
    print("finally...")     # 总会执行

# 捕获多种异常
try:
    r = 10 / int('abc')
except ValueError as e:
    print("ValueError:", e)
except ZeroDivisionError as e:
    print("ZeroDivisionError:", e)

# 异常的继承关系：父类能捕获子类异常
try:
    r = 10 / 0
except Exception as e:     # Exception 是大多数异常的父类
    print("捕获到:", type(e).__name__, e)

# else：没有异常时执行
try:
    r = 10 / 2
except ZeroDivisionError:
    print("除零错误")
else:
    print("没有异常，结果:", r)

# 使用 logging 记录异常（推荐！）
import logging

try:
    10 / 0
except Exception:
    logging.exception("出错了")    # 会打印完整堆栈

# 抛出异常
def check_age(age):
    if age < 0:
        raise ValueError(f"年龄不能为负数: {age}")
    return age

try:
    check_age(-1)
except ValueError as e:
    print("捕获:", e)

# 自定义异常
class FooError(ValueError):
    pass

try:
    raise FooError("自定义异常")
except FooError as e:
    print("FooError:", e)

# 异常链：raise ... from ...
try:
    try:
        1 / 0
    except ZeroDivisionError as e:
        raise RuntimeError("计算失败") from e
except RuntimeError as e:
    print(f"{e}，原因: {e.__cause__}")
