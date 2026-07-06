# __slots__

from types import MethodType


print("=== 普通类可以动态绑定属性 ===")


class Student:
    # 不定义 __slots__ 的普通类，实例会有 __dict__ 保存动态属性。
    pass


student = Student()
# 普通实例可以在运行时新增任意属性。
student.name = "Alice"
student.age = 18
print(student.name, student.age)
print(hasattr(student, "__dict__"))


print("\n=== 普通实例还能动态绑定方法 ===")


def set_score(self, score):
    self.score = score


# MethodType 可以把函数绑定成某个实例的方法。
student.set_score = MethodType(set_score, student)
student.set_score(99)
print(student.score)


print("\n=== __slots__ 限制实例属性 ===")


class Person:
    # __slots__ 限制实例只能拥有这些属性，并且通常不再生成 __dict__。
    __slots__ = ("name", "age")


person = Person()
person.name = "Bob"
person.age = 25
print(person.name, person.age)
print(hasattr(person, "__dict__"))

try:
    # score 不在 __slots__ 里，所以不能动态新增。
    person.score = 99
except AttributeError as error:
    print(type(error).__name__)


print("\n=== __slots__ 默认不限制子类 ===")


class GraduateStudent(Person):
    # 子类没有定义 __slots__ 时，会重新拥有 __dict__。
    pass


graduate = GraduateStudent()
graduate.name = "Charlie"
graduate.score = 100
print(graduate.name, graduate.score)
print(hasattr(graduate, "__dict__"))


print("\n=== 子类也定义 __slots__ ===")


class UnderGrad(Person):
    # 子类也定义 __slots__，才能继续限制新增属性。
    __slots__ = ("score",)


under_grad = UnderGrad()
under_grad.name = "Dave"
under_grad.age = 20
under_grad.score = 88
print(under_grad.name, under_grad.age, under_grad.score)
print(hasattr(under_grad, "__dict__"))

try:
    under_grad.gpa = 3.8
except AttributeError as error:
    print(type(error).__name__)
