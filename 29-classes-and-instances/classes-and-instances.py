# 类和实例

# 定义类
class Student:
    def __init__(self, name, score):
        self.name = name      # 实例属性
        self.score = score

    def print_score(self):
        print(f"{self.name}: {self.score}")

    def get_grade(self):
        if self.score >= 90:
            return 'A'
        elif self.score >= 60:
            return 'B'
        else:
            return 'C'

# 创建实例
bart = Student('Bart Simpson', 59)
lisa = Student('Lisa Simpson', 87)

bart.print_score()
lisa.print_score()
print(f"{bart.name} 的等级: {bart.get_grade()}")

# 可以自由给实例绑定属性
bart.age = 10
print(bart.age)

# 类也是对象
print(type(bart))       # <class '__main__.Student'>
print(isinstance(bart, Student))  # True
