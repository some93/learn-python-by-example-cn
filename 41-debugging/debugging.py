# 调试

import logging
import sys


print("=== print 调试 ===")


def calc(a, b):
    # print 调试最直接，但临时输出多了以后很难管理。
    print(f"DEBUG: a={a}, b={b}")
    return a + b


print(calc(1, 2))  # DEBUG: a=1, b=2 / 3


print("\n=== assert 断言 ===")


def div(a, b):
    # assert 适合表达“开发阶段必须成立”的条件。
    assert b != 0, "除数不能为零"
    return a / b


print(div(10, 2))  # 5.0

try:
    div(10, 0)
except AssertionError as error:
    print(type(error).__name__, error)  # AssertionError 除数不能为零


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


print(process_data(["1", "2", "abc", "4"]))  # [1, 2, 4]


print("\n=== pdb 和 IDE 调试 ===")

print("pdb.set_trace() 可以设置命令行断点")
print("VSCode / PyCharm 可以设置可视化断点")
