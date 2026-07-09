# @property


print("=== 直接暴露属性的问题 ===")


class BadStudent:
    pass


bad = BadStudent()
# 直接暴露属性时，外部可以写入明显不合理的值。
bad.score = 9999
print(bad.score)  # 9999


print("\n=== 老式 getter/setter ===")


class OldStudent:
    def get_score(self):
        return self._score

    def set_score(self, value):
        # getter/setter 可以校验数据，但调用方式比较啰嗦。
        if not isinstance(value, int):
            raise ValueError("分数必须是整数")
        if value < 0 or value > 100:
            raise ValueError("分数必须在 0-100 之间")
        self._score = value


old = OldStudent()
old.set_score(88)
print(old.get_score())  # 88


print("\n=== @property 读写属性 ===")


class Student:
    @property
    def score(self):
        # @property 让方法像属性一样读取。
        return self._score

    @score.setter
    def score(self, value):
        # setter 保留校验能力，同时调用方式变成 student.score = ...
        if not isinstance(value, int):
            raise ValueError("分数必须是整数")
        if value < 0 or value > 100:
            raise ValueError("分数必须在 0-100 之间")
        self._score = value


student = Student()
student.score = 90
print(student.score)  # 90

try:
    student.score = 120
except ValueError as error:
    print(error)  # 分数必须在 0-100 之间


print("\n=== 只读属性和计算属性 ===")


class Person:
    def __init__(self, birth_year, current_year):
        self._birth_year = birth_year
        self._current_year = current_year

    @property
    def birth_year(self):
        # 只定义 getter，没有 setter，就是只读属性。
        return self._birth_year

    @property
    def age(self):
        # 计算属性不一定需要真实存储在对象里。
        return self._current_year - self._birth_year


person = Person(2000, 2026)
print(person.birth_year)  # 2000
print(person.age)  # 26

try:
    person.age = 30
except AttributeError as error:
    print(type(error).__name__)  # AttributeError
