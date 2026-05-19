# @property

# 直接暴露属性没有参数检查
class BadStudent:
    pass

s = BadStudent()
s.score = 9999   # 没有检查，可以随便设

# 用 getter/setter 方法能检查，但调用不方便
class OldStudent:
    def get_score(self):
        return self._score

    def set_score(self, value):
        if not isinstance(value, int):
            raise ValueError('分数必须是整数')
        if value < 0 or value > 100:
            raise ValueError('分数必须在 0-100 之间')
        self._score = value

# 用 @property 两全其美！
class Student:
    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('分数必须是整数')
        if value < 0 or value > 100:
            raise ValueError('分数必须在 0-100 之间')
        self._score = value

s = Student()
s.score = 88      # 像属性一样赋值，实际调用 setter
print(s.score)     # 像属性一样读取，实际调用 getter

# s.score = 9999  # ValueError!

# 只读属性：只定义 getter，不定义 setter
class Person:
    def __init__(self, birth_year):
        self._birth_year = birth_year

    @property
    def birth_year(self):
        return self._birth_year

    @property
    def age(self):
        import datetime
        return datetime.datetime.now().year - self._birth_year

p = Person(2000)
print(p.age)          # 根据当前年份计算
# p.age = 30          # AttributeError! 只读属性
print(p.birth_year)   # 2000
