# 类和实例


print("=== 定义类和创建实例 ===")


class Student:
    # class 内、方法外定义的是类属性，所有实例默认共享。
    school = "Springfield School"

    def __init__(self, name, score):
        # self 指向当前实例，这里给每个学生保存自己的数据。
        self.name = name
        self.score = score

    def print_score(self):
        print(f"{self.name}: {self.score}")

    def get_grade(self):
        # 方法可以直接读取实例属性，封装和学生相关的业务逻辑。
        if self.score >= 90:
            return "A"
        if self.score >= 60:
            return "B"
        return "C"

    def update_score(self, score):
        self.score = score


bart = Student("Bart Simpson", 59)
lisa = Student("Lisa Simpson", 87)

# 调用实例方法时，Python 会自动把实例作为 self 传进去。
bart.print_score()
lisa.print_score()
print(f"{bart.name} 的等级: {bart.get_grade()}")
print(f"{lisa.name} 的等级: {lisa.get_grade()}")


print("\n=== self 是实例自身 ===")

# 下面这行等价于 bart.print_score()，只是手动把 bart 传给 self。
Student.print_score(bart)
bart.update_score(75)
bart.print_score()
print(bart.get_grade())


print("\n=== 实例属性和类属性 ===")

print(bart.name)
# 实例找不到 school 时，会继续去类上找。
print(bart.school)
print(lisa.school)

# 修改类属性会影响还没有被实例属性遮蔽的所有实例。
Student.school = "Python School"
print(bart.school)
print(lisa.school)


print("\n=== 动态绑定实例属性 ===")

# Python 普通类的实例默认可以随时新增属性。
bart.age = 10
print(bart.age)
print(hasattr(lisa, "age"))


print("\n=== 类型判断 ===")

print(type(bart).__name__)
print(isinstance(bart, Student))
