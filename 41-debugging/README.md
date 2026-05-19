# 第 41 关：调试（师兄带你学 Python）

## 🎯 这一关你会学到

- 了解 `print` 调试法
- 使用 `assert` 断言
- 使用 `logging` 模块（推荐）
- 了解 `pdb` 和 IDE 调试

## 🤔 先想一个问题

程序出了 bug，你怎么找原因？最原始的方法是到处加 `print`，但这就像在黑屋子里用打火机找东西。有没有更好的「手电筒」？

带着这个问题，我们来看代码。

## 📖 看代码

```python
# 调试

# 方法一：print()（最简单但最原始）
def calc(a, b):
    print(f"DEBUG: a={a}, b={b}")   # 调试用
    return a + b

calc(1, 2)

# 方法二：assert（断言）
def div(a, b):
    assert b != 0, "除数不能为零！"
    return a / b

print(div(10, 2))
# div(10, 0)   # AssertionError: 除数不能为零！

# 启动时可以关闭 assert：python -O debugging.py

# 方法三：logging（推荐！）
import logging
logging.basicConfig(level=logging.DEBUG)

logging.debug("这是 debug 信息")
logging.info("这是 info 信息")
logging.warning("这是 warning 信息")
logging.error("这是 error 信息")

# 日志级别：DEBUG < INFO < WARNING < ERROR < CRITICAL
# 设置 level=logging.INFO 就不会输出 DEBUG 级别的信息

# 方法四：pdb（交互式调试器）
# import pdb
# pdb.set_trace()    # 在这里设断点

# pdb 常用命令：
# l (list)     查看代码
# n (next)     下一步
# p 变量名      打印变量
# c (continue) 继续执行
# q (quit)     退出

# 方法五：IDE 调试（最方便）
# VSCode、PyCharm 都支持可视化断点调试

# 实际项目中的 logging 配置
logger = logging.getLogger(__name__)

def process_data(data):
    logger.info(f"开始处理数据，共 {len(data)} 条")
    result = []
    for item in data:
        try:
            result.append(int(item))
        except ValueError:
            logger.warning(f"无法转换: {item}")
    logger.info(f"处理完成，成功 {len(result)} 条")
    return result

process_data(['1', '2', 'abc', '4', 'xyz'])
```

## 🔍 师兄给你逐行拆

> 代码已经在注释中做了详细说明，这里挑重点讲。

### 核心要点

- `print` 调试要记得事后删掉，不然代码里全是垃圾输出
- `assert` 可以用 `python -O` 全局关闭，所以别用它做业务检查
- `logging` 是最推荐的方式：可以分级别、可以输出到文件、可以随时关闭
- `pdb` 适合排查复杂 bug，但学习成本比 IDE 调试高
- 实际项目中用 `logging.getLogger(__name__)` 创建模块级 logger

## 🏃 跑一下试试

```bash
cd 41-debugging
python debugging.py
```

## 💡 师兄的碎碎念

- `print` 调试要记得事后删掉，不然代码里全是垃圾输出
- `assert` 可以用 `python -O` 全局关闭，所以别用它做业务检查
- `logging` 是最推荐的方式：可以分级别、可以输出到文件、可以随时关闭
- `pdb` 适合排查复杂 bug，但学习成本比 IDE 调试高
- 实际项目中用 `logging.getLogger(__name__)` 创建模块级 logger

## 🎓 这一关的知识点清单

| 知识点 | 说明 |
|--------|------|
| `print()` | 最简单的调试方法 |
| `assert expr, msg` | 断言，条件不满足时抛出 AssertionError |
| `logging.debug/info/warning/error` | 分级别的日志输出 |
| `logging.basicConfig(level=...)` | 设置日志级别 |
| `pdb.set_trace()` | 设置断点，进入交互调试 |

## ➡️ 下一关

下一关我们学习 [单元测试](../42-unit-testing/README.md)，继续加油！
