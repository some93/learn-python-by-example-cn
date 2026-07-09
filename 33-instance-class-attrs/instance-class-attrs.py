# 实例属性和类属性


print("=== 类属性和实例属性 ===")


class Student:
    # 类属性属于类对象，实例没有同名属性时会读到它。
    school = "清华大学"

    def __init__(self, name):
        # 实例属性属于某个具体对象。
        self.name = name


s1 = Student("Alice")
s2 = Student("Bob")

print(Student.school)  # 清华大学
print(s1.school)  # 清华大学
print(s2.school)  # 清华大学
print(s1.name)  # Alice
print(s2.name)  # Bob


print("\n=== 实例属性遮蔽类属性 ===")

# 给 s1 绑定同名实例属性后，s1.school 会优先读实例自己的值。
s1.school = "北京大学"
print(s1.school)  # 北京大学
print(s2.school)  # 清华大学
print(Student.school)  # 清华大学
print("school" in s1.__dict__)  # True
print("school" in s2.__dict__)  # False

# 删除实例属性后，再次读取会回到类属性。
del s1.school
print(s1.school)  # 清华大学


print("\n=== 修改类属性 ===")

# 修改类属性会影响所有没有同名实例属性的对象。
Student.school = "Python 大学"
print(s1.school)  # Python 大学
print(s2.school)  # Python 大学
print(Student.school)  # Python 大学


print("\n=== 类属性计数器 ===")


class Counter:
    count = 0

    def __init__(self):
        # 用类名访问类属性，表达“所有实例共享一个计数器”。
        Counter.count += 1


Counter()
Counter()
Counter()
print(Counter.count)  # 3


print("\n=== 可变类属性的坑 ===")


class BadBag:
    # 可变类属性会被所有实例共享，容易造成数据串在一起。
    items = []

    def add(self, item):
        self.items.append(item)


bag1 = BadBag()
bag2 = BadBag()
bag1.add("苹果")
bag2.add("香蕉")
print(bag1.items)  # ['苹果', '香蕉']
print(bag2.items)  # ['苹果', '香蕉']
print(bag1.items is bag2.items)  # True


print("\n=== 正确做法：可变数据放实例属性 ===")


class GoodBag:
    def __init__(self):
        # 每个实例都创建自己的列表，互不影响。
        self.items = []

    def add(self, item):
        self.items.append(item)


good1 = GoodBag()
good2 = GoodBag()
good1.add("苹果")
good2.add("香蕉")
print(good1.items)  # ['苹果']
print(good2.items)  # ['香蕉']
print(good1.items is good2.items)  # False
