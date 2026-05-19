# 实例属性和类属性

class Student:
    # 类属性：所有实例共享
    school = '清华大学'

    def __init__(self, name):
        # 实例属性：每个实例独立
        self.name = name

s1 = Student('Alice')
s2 = Student('Bob')

# 访问类属性
print(Student.school)    # 清华大学
print(s1.school)         # 清华大学（通过实例也能访问）
print(s2.school)         # 清华大学

# 实例属性互不影响
print(s1.name)    # Alice
print(s2.name)    # Bob

# 注意：实例属性会"遮蔽"同名的类属性
s1.school = '北京大学'   # 这是给 s1 加了一个实例属性！
print(s1.school)         # 北京大学（实例属性）
print(s2.school)         # 清华大学（类属性不受影响）
print(Student.school)    # 清华大学

# 删掉实例属性后，又能看到类属性了
del s1.school
print(s1.school)         # 清华大学

# 用类属性做计数器
class Counter:
    count = 0

    def __init__(self):
        Counter.count += 1    # 用类名访问，而不是 self

c1 = Counter()
c2 = Counter()
c3 = Counter()
print(Counter.count)    # 3
