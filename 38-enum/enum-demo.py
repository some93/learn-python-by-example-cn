# 枚举类

from enum import Enum, IntEnum, unique


print("=== 快捷创建枚举 ===")

# Enum() 可以快速创建枚举类，第二个参数是成员名列表。
Month = Enum(
    "Month",
    ("Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"),
)

print(Month.Jan)
print(Month.Jan.name)
# 默认 value 从 1 开始递增。
print(Month.Jan.value)
print(Month["Jan"])
print(Month(1))


print("\n=== 继承 Enum 定义枚举 ===")


@unique
class Weekday(Enum):
    # 继承 Enum 的写法更适合业务代码，成员名和值一眼可见。
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6
    Sun = 7


day = Weekday.Sat
print(day)
print(day.name)
print(day.value)
# 可以按名字或按值反向获取枚举成员。
print(Weekday["Sat"])
print(Weekday(6))


print("\n=== 遍历枚举 ===")

for member in Weekday:
    # 遍历枚举时拿到的是枚举成员，不是普通字符串或整数。
    print(f"{member.name} => {member.value}")


print("\n=== 枚举比较 ===")

print(Weekday.Mon == Weekday.Mon)
print(Weekday.Mon == Weekday.Tue)
print(Weekday.Mon is Weekday.Mon)
# 普通 Enum 不会直接等于它的 value。
print(Weekday.Mon == 1)


print("\n=== IntEnum 可以和整数比较 ===")


class HttpStatus(IntEnum):
    # IntEnum 适合需要和整数兼容的场景，例如 HTTP 状态码。
    OK = 200
    NOT_FOUND = 404
    SERVER_ERROR = 500


print(HttpStatus.OK == 200)
print(HttpStatus.NOT_FOUND > HttpStatus.OK)


print("\n=== @unique 检查重复值 ===")

try:
    # @unique 会在类创建时检查重复 value。
    @unique
    class BadStatus(Enum):
        SUCCESS = 1
        OK = 1
except ValueError as error:
    print(type(error).__name__)


print("\n=== match 中使用枚举 ===")

status = Weekday.Sat

match status:
    # match/case 可以直接匹配枚举成员。
    case Weekday.Sat | Weekday.Sun:
        print("周末")
    case _:
        print("工作日")
