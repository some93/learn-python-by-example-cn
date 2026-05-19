# __slots__

# 正常情况下，可以给实例绑定任意属性
class Student:
    pass

s = Student()
s.name = 'Alice'      # 动态绑定属性
s.age = 18
print(s.name, s.age)

# 甚至可以绑定方法
from types import MethodType

def set_score(self, score):
    self.score = score

s.set_score = MethodType(set_score, s)
s.set_score(99)
print(s.score)    # 99

# 用 __slots__ 限制实例属性
class Person:
    __slots__ = ('name', 'age')   # 只允许绑定 name 和 age

p = Person()
p.name = 'Bob'
p.age = 25
# p.score = 99   # AttributeError! 不允许绑定 score

# __slots__ 对子类不起作用（除非子类也定义 __slots__）
class GraduateStudent(Person):
    pass

g = GraduateStudent()
g.name = 'Charlie'
g.score = 100     # 可以！子类没有 __slots__ 限制
print(g.score)

# 子类也定义 __slots__ 时，子类允许的属性是两者的并集
class UnderGrad(Person):
    __slots__ = ('score',)   # 加上父类的 name、age，共三个

u = UnderGrad()
u.name = 'Dave'
u.age = 20
u.score = 88
# u.gpa = 3.8   # AttributeError!

# __slots__ 的好处：节省内存（不用 __dict__）
print(hasattr(p, '__dict__'))    # False（有 __slots__ 就没有 __dict__）
print(hasattr(s, '__dict__'))    # True（普通类有 __dict__）
