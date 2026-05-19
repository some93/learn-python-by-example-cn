# 访问限制

class Student:
    def __init__(self, name, score):
        self.__name = name      # 双下划线开头：私有属性
        self.__score = score

    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score

    def set_score(self, score):
        if 0 <= score <= 100:
            self.__score = score
        else:
            raise ValueError('分数必须在 0-100 之间')

    def print_info(self):
        print(f"{self.__name}: {self.__score}")

bart = Student('Bart', 59)
bart.print_info()

# 不能直接访问私有属性
# print(bart.__name)  # AttributeError!

# 通过 getter/setter 访问
print(bart.get_name())
bart.set_score(80)
bart.print_info()

# Python 的"私有"是名字改编，不是真正的访问控制
# 实际上可以通过 _类名__属性名 访问（但不要这样做！）
print(bart._Student__name)    # Bart（能访问但别这么干）

# 单下划线 _xxx：约定私有，外部可以访问但不建议
# 双下划线 __xxx：名字改编为 _ClassName__xxx
# __xxx__：特殊变量（如 __init__），不是私有的
