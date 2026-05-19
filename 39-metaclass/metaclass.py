# 元类（Metaclass）

# type() 不仅能查类型，还能动态创建类！

# 常规定义
class Hello:
    def hello(self):
        print("Hello, world!")

# 等价于用 type() 创建
def hello_func(self):
    print("Hello, world!")

Hello2 = type('Hello2', (object,), {'hello': hello_func})

h = Hello2()
h.hello()    # Hello, world!
# type(类名, (父类们,), {方法字典})

# metaclass：控制类的创建过程
# 最常见的用途：ORM（对象关系映射）

# 定义 metaclass
class ListMetaclass(type):
    def __new__(cls, name, bases, attrs):
        attrs['add'] = lambda self, value: self.append(value)
        return type.__new__(cls, name, bases, attrs)

# 使用 metaclass
class MyList(list, metaclass=ListMetaclass):
    pass

L = MyList()
L.add(1)     # metaclass 自动添加的方法
L.add(2)
L.add(3)
print(L)     # [1, 2, 3]

# 简易 ORM 示例
class Field:
    def __init__(self, name, column_type):
        self.name = name
        self.column_type = column_type

    def __str__(self):
        return f"<{self.__class__.__name__}:{self.name}>"

class StringField(Field):
    def __init__(self, name):
        super().__init__(name, 'varchar(100)')

class IntegerField(Field):
    def __init__(self, name):
        super().__init__(name, 'bigint')

class ModelMetaclass(type):
    def __new__(cls, name, bases, attrs):
        if name == 'Model':
            return type.__new__(cls, name, bases, attrs)
        print(f"创建模型: {name}")
        mappings = {}
        for k, v in attrs.items():
            if isinstance(v, Field):
                print(f"  映射字段: {k} ==> {v}")
                mappings[k] = v
        for k in mappings:
            attrs.pop(k)
        attrs['__mappings__'] = mappings
        attrs['__table__'] = name
        return type.__new__(cls, name, bases, attrs)

class Model(dict, metaclass=ModelMetaclass):
    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(f"'Model' 没有属性 '{key}'")

    def __setattr__(self, key, value):
        self[key] = value

    def save(self):
        fields = []
        params = []
        for k, v in self.__mappings__.items():
            fields.append(v.name)
            params.append(str(getattr(self, k, None)))
        sql = f"INSERT INTO {self.__table__} ({','.join(fields)}) VALUES ({','.join(params)})"
        print(f"SQL: {sql}")

# 使用 ORM
class User(Model):
    id = IntegerField('id')
    name = StringField('username')
    email = StringField('email')

u = User(id=1, name='Alice', email='alice@example.com')
u.save()
