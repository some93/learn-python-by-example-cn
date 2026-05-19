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
