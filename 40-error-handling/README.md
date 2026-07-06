# 第 40 关：错误处理（师兄带你学 Python）

## 🎯 这一关你会学到

- `try / except / else / finally` 的执行顺序
- 如何捕获不同类型的异常
- 异常类的继承关系
- 如何主动 `raise` 异常和自定义异常
- `raise ... from ...` 如何保留原始原因
- 为什么不要随便裸写 `except`

## 🤔 先想一个问题

你写了一个除法程序，用户输入 `0` 做除数，程序直接崩了。

你不可能保证用户永远不犯错，也不可能保证文件永远存在、网络永远通、数据永远干净。但你可以提前准备“兜底方案”：出错时给出清楚提示，释放资源，记录日志，而不是让程序原地爆炸。

这就是异常处理。

## 📖 看代码

```python
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
    print("except:", error)
finally:
    # finally 不管有没有异常都会执行，常用于释放资源。
    print("finally...")


print("\n=== 捕获多种异常 ===")

try:
    # int("abc") 会先抛出 ValueError，后面的除法不会执行。
    result = 10 / int("abc")
except ValueError as error:
    print("ValueError:", error)
except ZeroDivisionError as error:
    print("ZeroDivisionError:", error)


print("\n=== else：没有异常时执行 ===")

try:
    result = 10 / 2
except ZeroDivisionError:
    print("除零错误")
else:
    # else 只在 try 没有异常时执行。
    print("没有异常，结果:", result)
finally:
    print("清理资源")


print("\n=== 异常继承关系 ===")

try:
    10 / 0
except Exception as error:
    # Exception 能捕获大多数业务异常，但不要无脑吞掉错误。
    print(type(error).__name__)


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
    print("捕获:", error)


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
    print("AgeError:", error)


print("\n=== 异常链 raise from ===")

try:
    try:
        1 / 0
    except ZeroDivisionError as error:
        # raise from 会保留原始异常，方便定位根因。
        raise RuntimeError("计算失败") from error
except RuntimeError as error:
    print(error)
    print(type(error.__cause__).__name__)


print("\n=== 重新抛出异常 ===")

try:
    try:
        check_age(-5)
    except ValueError:
        print("记录后继续抛出")
        # 单独写 raise 表示重新抛出当前异常。
        raise
except ValueError as error:
    print("外层捕获:", error)
```

## 🔍 师兄给你逐行拆

### `try / except / finally`

```python
try:
    print("try...")
    result = 10 / 0
    print("结果:", result)
except ZeroDivisionError as error:
    print("except:", error)
finally:
    print("finally...")
```

**这行在干嘛？**

`try` 里放可能出错的代码。`10 / 0` 会抛出 `ZeroDivisionError`，所以后面的 `print("结果:", result)` 不会执行。

Python 跳到对应的 `except ZeroDivisionError`，把异常对象保存到 `error`。

最后无论是否出错，`finally` 都会执行。

**什么时候用 finally？**

释放资源时最常用：关闭文件、释放锁、断开连接、清理临时状态。

---

### 捕获多种异常

```python
try:
    result = 10 / int("abc")
except ValueError as error:
    print("ValueError:", error)
except ZeroDivisionError as error:
    print("ZeroDivisionError:", error)
```

**这行在干嘛？**

`int("abc")` 会先抛出 `ValueError`，所以除法根本还没执行。

多个 `except` 会从上到下匹配，匹配到第一个合适的就执行。

**容易踩的坑**

更宽泛的异常类型要放后面。比如 `Exception` 是很多异常的父类，如果你把它放最前面，后面的 `ValueError`、`ZeroDivisionError` 就永远轮不到。

---

### `else`：没有异常时执行

```python
try:
    result = 10 / 2
except ZeroDivisionError:
    print("除零错误")
else:
    print("没有异常，结果:", result)
finally:
    print("清理资源")
```

**这行在干嘛？**

`else` 只在 `try` 代码块没有异常时执行。

这能把“正常路径”和“异常处理路径”分开，看起来更清楚。

执行顺序可以记成：

```text
try 成功 -> else -> finally
try 失败 -> except -> finally
```

---

### 异常继承关系

```python
try:
    10 / 0
except Exception as error:
    print(type(error).__name__)
```

**这行在干嘛？**

`ZeroDivisionError` 是 `Exception` 的子类，所以能被 `except Exception` 捕获。

**为什么别捕获 `BaseException`？**

`BaseException` 还包括 `KeyboardInterrupt`、`SystemExit` 这种系统级异常。你通常不该拦住用户 Ctrl+C 或程序退出信号。

业务代码一般最多捕获 `Exception`，更好是捕获明确异常类型。

---

### logging 记录异常

```python
try:
    int("not-a-number")
except ValueError as error:
    logging.error("转换失败: %s", error)
```

**这行在干嘛？**

这里用日志记录错误，而不是简单 `print()`。

真实项目中，如果想记录完整堆栈，常用：

```python
logging.exception("转换失败")
```

它会在 `except` 块里自动记录当前异常的 traceback。教程示例为了输出稳定，只打印一行错误日志。

---

### 主动抛出异常

```python
def check_age(age):
    if age < 0:
        raise ValueError(f"年龄不能为负数: {age}")
    return age
```

**这行在干嘛？**

函数发现参数非法时，主动 `raise ValueError`。这比返回一个奇怪的值更清楚。

**为什么不用 `return False`？**

年龄为负数不是正常业务结果，而是调用方传错参数。用异常能让错误更明显，也能携带具体原因。

---

### 自定义异常

```python
class AgeError(ValueError):
    pass
```

**这行在干嘛？**

自定义一个 `AgeError`，表示年龄相关错误。它继承 `ValueError`，说明本质还是“值不合法”。

**为什么要自定义？**

当你的业务错误种类变多时，自定义异常能让调用方精准捕获：

```python
except AgeError:
    ...
```

而不是把所有 `ValueError` 混在一起处理。

---

### 异常链：`raise ... from ...`

```python
try:
    1 / 0
except ZeroDivisionError as error:
    raise RuntimeError("计算失败") from error
```

**这行在干嘛？**

底层错误是 `ZeroDivisionError`，但你想对外抛出更业务化的 `RuntimeError("计算失败")`。

`from error` 会保留原始原因，放在新异常的 `__cause__` 里。

这样既能给上层更清楚的业务错误，又不丢掉底层线索。

---

### 重新抛出异常

```python
except ValueError:
    print("记录后继续抛出")
    raise
```

**这行在干嘛？**

`raise` 不带参数，表示把当前捕获到的异常原样重新抛出去。

常见场景是：这一层只负责记录日志或补充上下文，不负责吞掉错误。

**容易踩的坑**

不要写裸 `except:` 然后什么都不做：

```python
try:
    ...
except:
    pass
```

这会把真正的 bug 全吞掉，后面排查会非常痛苦。

## 🏃 跑一下试试

```bash
$ python error-handling.py
=== try / except / finally ===
try...
except: division by zero
finally...

=== 捕获多种异常 ===
ValueError: invalid literal for int() with base 10: 'abc'

=== else：没有异常时执行 ===
没有异常，结果: 5.0
清理资源

=== 异常继承关系 ===
ZeroDivisionError

=== logging 记录异常 ===
ERROR:转换失败: invalid literal for int() with base 10: 'not-a-number'

=== 主动抛出异常 ===
捕获: 年龄不能为负数: -1

=== 自定义异常 ===
AgeError: 未成年人不能注册

=== 异常链 raise from ===
计算失败
ZeroDivisionError

=== 重新抛出异常 ===
记录后继续抛出
外层捕获: 年龄不能为负数: -5
```

## 💡 师兄的碎碎念

- `finally` 总会执行，适合做清理工作。
- 多个 `except` 从上往下匹配，具体异常放前面，宽泛异常放后面。
- `else` 表示 try 成功后的正常路径。
- 自定义异常建议继承 `Exception` 或其子类，不要继承 `BaseException`。
- 不要裸 `except: pass`，这会隐藏真正的 bug。

## 🎓 这一关的知识点清单

- **try**：包住可能出错的代码。
- **except**：捕获并处理指定类型的异常。
- **else**：没有异常时执行。
- **finally**：无论是否异常都执行。
- **raise**：主动抛出异常；不带参数时重新抛出当前异常。
- **自定义异常**：用类表达业务错误类型。
- **异常链**：`raise NewError from old_error` 保留原始原因。

## ➡️ 下一关

错误能兜住还不够，bug 还得找出来。下一关看调试：print、assert、logging、pdb 和 IDE 调试怎么选 👉 [下一关：调试 →](../41-debugging/)


