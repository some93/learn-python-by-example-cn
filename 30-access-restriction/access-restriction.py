# 访问限制


print("=== 私有属性和公开方法 ===")


class Student:
    def __init__(self, name, score):
        # 双下划线开头会触发名字改编，外部不能直接用 __name 访问。
        self.__name = name
        self.__score = score

        # 单下划线只是约定私有，语法上仍然能访问。
        self._school = "Springfield School"

    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score

    def set_score(self, score):
        # 通过 setter 统一校验，避免外部随便写入非法值。
        if not 0 <= score <= 100:
            raise ValueError("分数必须在 0-100 之间")
        self.__score = score

    def print_info(self):
        print(f"{self.__name}: {self.__score}")


bart = Student("Bart", 59)
bart.print_info()
print(bart.get_name())
print(bart.get_score())

bart.set_score(80)
bart.print_info()


print("\n=== setter 负责校验 ===")

try:
    bart.set_score(120)
except ValueError as error:
    print(error)


print("\n=== 不能直接访问双下划线属性 ===")

try:
    # 外部没有 bart.__name 这个属性名。
    print(bart.__name)
except AttributeError as error:
    print(type(error).__name__)


print("\n=== 名字改编：能访问，但不该访问 ===")

# Python 会把 __name 改成 _类名__name，目的是避免意外访问。
print(bart._Student__name)
print(bart._Student__score)


print("\n=== 三种下划线写法 ===")

print(bart._school)
print(hasattr(bart, "__name"))
print(hasattr(bart, "_Student__name"))
# __init__ 这种首尾双下划线是特殊方法，不属于私有属性。
print(Student.__init__.__name__)
