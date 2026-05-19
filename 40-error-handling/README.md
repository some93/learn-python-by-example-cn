# 第 40 关：错误处理（师兄带你学 Python）

## 🎯 这一关你会学到

- 掌握 `try...except...finally` 语法
- 捕获多种异常
- 使用 `logging` 记录异常
- 抛出和自定义异常

## 🤔 先想一个问题

你写了个除法程序，用户输入 0 做除数，程序直接崩了。你不可能保证用户永远不犯错，但你可以提前「兜住」错误，优雅地处理它。这就是**异常处理**。

带着这个问题，我们来看代码。

## 📖 看代码

```python
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
```

## 🔍 师兄给你逐行拆

> 代码已经在注释中做了详细说明，这里挑重点讲。

### 核心要点

- `finally` 里的代码无论是否异常都会执行，适合做清理工作
- `except Exception` 能捕获大多数异常，但别捕获 `BaseException`
- 用 `logging.exception()` 记录异常比 `print` 好得多
- `raise` 不带参数可以重新抛出当前异常
- 自定义异常要继承 `Exception` 或其子类，别继承 `BaseException`

## 🏃 跑一下试试

```bash
cd 40-error-handling
python error-handling.py
```

## 💡 师兄的碎碎念

- `finally` 里的代码无论是否异常都会执行，适合做清理工作
- `except Exception` 能捕获大多数异常，但别捕获 `BaseException`
- 用 `logging.exception()` 记录异常比 `print` 好得多
- `raise` 不带参数可以重新抛出当前异常
- 自定义异常要继承 `Exception` 或其子类，别继承 `BaseException`

## 🎓 这一关的知识点清单

| 知识点 | 说明 |
|--------|------|
| `try...except...finally` | 异常捕获的完整语法 |
| `except XxxError as e` | 捕获特定类型的异常 |
| `else` | 没有异常时执行的代码块 |
| `raise ValueError(...)` | 主动抛出异常 |
| `class MyError(Exception)` | 自定义异常类 |
| `raise ... from ...` | 异常链，保留原始异常信息 |

## ➡️ 下一关

下一关我们学习 [调试](../41-debugging/README.md)，继续加油！
