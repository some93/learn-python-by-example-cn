# Python 3.10+ 的 match/case 模式匹配

# 基本用法：匹配常量
status = 404

match status:
    case 200:
        print("OK")
    case 404:
        print("Not Found")
    case 500:
        print("Internal Server Error")
    case _:
        print(f"Unknown status: {status}")

# 匹配多个值（用 | 分隔）
command = "quit"

match command:
    case "quit" | "exit" | "q":
        print("退出程序")
    case "help" | "h":
        print("显示帮助")
    case _:
        print(f"未知命令: {command}")

# 匹配序列（列表/元组解构）
point = (0, 5)

match point:
    case (0, 0):
        print("原点")
    case (x, 0):
        print(f"在 x 轴上, x={x}")
    case (0, y):
        print(f"在 y 轴上, y={y}")
    case (x, y):
        print(f"任意点: ({x}, {y})")

# 带条件守卫（guard）的匹配
age = 15

match age:
    case n if n < 0:
        print("年龄不能为负")
    case n if n < 18:
        print(f"{n} 岁，未成年")
    case n if n < 60:
        print(f"{n} 岁，成年人")
    case _:
        print("老年人")
