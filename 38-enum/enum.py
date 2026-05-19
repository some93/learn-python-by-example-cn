# 枚举类

from enum import Enum, unique

# 定义枚举
Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
                        'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))

# 访问枚举成员
print(Month.Jan)          # Month.Jan
print(Month.Jan.value)    # 1（自动从 1 开始赋值）

# 遍历枚举
for name, member in Month.__members__.items():
    print(f"{name} => {member.value}")

# 自定义枚举类（推荐方式）
@unique   # 保证值不重复
class Weekday(Enum):
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6
    Sun = 7

# 多种访问方式
day = Weekday.Mon
print(day)              # Weekday.Mon
print(day.name)         # Mon
print(day.value)        # 1
print(Weekday(1))       # Weekday.Mon（通过值获取）
print(Weekday['Mon'])   # Weekday.Mon（通过名字获取）

# 枚举比较
print(Weekday.Mon == Weekday.Mon)    # True
print(Weekday.Mon == Weekday.Tue)    # False
# Weekday.Mon < Weekday.Tue          # TypeError! 枚举不支持大小比较

# 枚举用于 match
status = Weekday.Sat
match status:
    case Weekday.Sat | Weekday.Sun:
        print("周末！")
    case _:
        print("工作日")
