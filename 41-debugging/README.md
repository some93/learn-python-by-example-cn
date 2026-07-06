# 第 41 关：调试（师兄带你学 Python）

## 🎯 这一关你会学到

- `print()` 调试为什么简单但粗糙
- `assert` 断言适合检查程序内部假设
- `logging` 为什么比 print 更适合实际项目
- 日志级别 `DEBUG / INFO / WARNING / ERROR`
- `pdb` 和 IDE 断点调试各适合什么场景

## 🤔 先想一个问题

程序出了 bug，你怎么找原因？

最原始的方法是在代码里到处加 `print()`。这确实能用，但像在黑屋子里用打火机找钥匙：能照亮一点点，但容易把现场搞乱。

调试工具就是更稳定的手电筒：日志、断言、断点，各有用途。

## 📖 看代码

```python
# 调试

import logging
import sys


print("=== print 调试 ===")


def calc(a, b):
    # print 调试最直接，但临时输出多了以后很难管理。
    print(f"DEBUG: a={a}, b={b}")
    return a + b


print(calc(1, 2))


print("\n=== assert 断言 ===")


def div(a, b):
    # assert 适合表达“开发阶段必须成立”的条件。
    assert b != 0, "除数不能为零"
    return a / b


print(div(10, 2))

try:
    div(10, 0)
except AssertionError as error:
    print(type(error).__name__, error)


print("\n=== logging 日志 ===")

logging.basicConfig(level=logging.INFO, format="%(levelname)s:%(message)s", stream=sys.stdout)
logger = logging.getLogger("debugging-demo")

# 当前日志级别是 INFO，所以 DEBUG 不会显示。
logger.debug("这条 DEBUG 不会显示")
logger.info("开始处理")
logger.warning("发现可疑数据")
logger.error("发生错误")


print("\n=== 用 logging 处理数据 ===")


def process_data(data):
    logger.info("开始处理 %d 条数据", len(data))
    result = []
    for item in data:
        try:
            # 每条数据单独处理，坏数据不会影响后续数据。
            result.append(int(item))
        except ValueError:
            # 日志里带上失败项，方便之后排查。
            logger.warning("无法转换: %s", item)
    logger.info("处理完成，成功 %d 条", len(result))
    return result


print(process_data(["1", "2", "abc", "4"]))


print("\n=== pdb 和 IDE 调试 ===")

print("pdb.set_trace() 可以设置命令行断点")
print("VSCode / PyCharm 可以设置可视化断点")
```

## 🔍 师兄给你逐行拆

### `print()` 调试：最快，但要收拾现场

```python
def calc(a, b):
    print(f"DEBUG: a={a}, b={b}")
    return a + b
```

**这行在干嘛？**

在函数里打印中间变量，看看调用时 `a`、`b` 到底是什么。

**什么时候用？**

临时排查小问题时很好用。比如你刚写完一段代码，想快速确认变量值。

**容易踩的坑**

`print()` 调试要记得删除。否则项目里到处都是临时输出，真正的业务输出会被淹没。

---

### `assert`：检查程序内部假设

```python
def div(a, b):
    assert b != 0, "除数不能为零"
    return a / b
```

**这行在干嘛？**

`assert 条件, 信息` 表示：我认为这个条件必须成立。如果不成立，就抛出 `AssertionError`。

**重点提醒**

`assert` 可以被优化模式关闭：

```bash
python -O debugging.py
```

所以不要用 `assert` 做用户输入校验、权限校验、支付金额校验这种业务逻辑。

业务检查应该用正常的 `if` + `raise`。

---

### `logging`：项目里更推荐的调试输出

```python
logging.basicConfig(level=logging.INFO, format="%(levelname)s:%(message)s", stream=sys.stdout)
logger = logging.getLogger("debugging-demo")

logger.debug("这条 DEBUG 不会显示")
logger.info("开始处理")
logger.warning("发现可疑数据")
logger.error("发生错误")
```

**这行在干嘛？**

`logging` 支持日志级别。这里设置 `level=logging.INFO`，所以：

- `DEBUG` 不显示；
- `INFO`、`WARNING`、`ERROR` 会显示。

**为什么比 print 好？**

日志可以分级别、控制格式、输出到文件、按模块命名、线上关闭 debug。`print()` 做不到这些。

---

### 日志格式化别急着用 f-string

```python
logger.info("开始处理 %d 条数据", len(data))
logger.warning("无法转换: %s", item)
```

**这行在干嘛？**

这是 logging 推荐的格式化方式。它把模板和变量分开传给 logger。

**为什么这么写？**

当某个日志级别被关闭时，logging 可以避免一些不必要的字符串格式化成本。实际项目里更常见。

---

### `pdb`：命令行断点调试

```python
import pdb
pdb.set_trace()
```

**这行在干嘛？**

如果你把这两行放进代码，程序运行到这里会暂停，进入交互式调试器。

常用命令：

```text
l      查看附近代码
n      执行下一行
s      进入函数
p x    打印变量 x
c      继续运行
q      退出调试
```

教程代码里没有真的打开 `pdb.set_trace()`，否则运行示例会卡住等待输入。

---

### IDE 调试：更适合新手和复杂流程

VSCode、PyCharm 都支持点击行号设置断点，然后一步步执行代码、查看变量、调用栈和表达式。

如果你刚开始学，IDE 调试通常比 `pdb` 更直观。

## 🏃 跑一下试试

```bash
$ python debugging.py
=== print 调试 ===
DEBUG: a=1, b=2
3

=== assert 断言 ===
5.0
AssertionError 除数不能为零

=== logging 日志 ===
INFO:开始处理
WARNING:发现可疑数据
ERROR:发生错误

=== 用 logging 处理数据 ===
INFO:开始处理 4 条数据
WARNING:无法转换: abc
INFO:处理完成，成功 3 条
[1, 2, 4]

=== pdb 和 IDE 调试 ===
pdb.set_trace() 可以设置命令行断点
VSCode / PyCharm 可以设置可视化断点
```

## 💡 师兄的碎碎念

- `print()` 适合临时看变量，但不要长期留在业务代码里。
- `assert` 适合检查内部假设，不适合做业务校验。
- `logging` 是实际项目的主力调试和运行记录工具。
- 日志级别从低到高是 `DEBUG < INFO < WARNING < ERROR < CRITICAL`。
- 断点调试适合看复杂流程，尤其是循环、递归、状态变化。

## 🎓 这一关的知识点清单

- **print 调试**：快速但粗糙的临时调试方法。
- **assert**：断言内部假设，不成立时抛 `AssertionError`。
- **logging**：标准日志模块，支持级别、格式、输出位置。
- **logger**：日志记录器，实际项目通常按模块创建。
- **pdb**：Python 内置命令行调试器。
- **IDE 断点**：图形化调试方式，适合复杂流程排查。

## ➡️ 下一关

调试是找 bug，测试是防 bug 回来。下一关看单元测试：用代码自动验证代码 👉 [下一关：单元测试 →](../42-unit-testing/)


