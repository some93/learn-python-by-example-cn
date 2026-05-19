# 第 39 关：元类（师兄带你学 Python）

## 🎯 这一关你会学到

- 理解 `type()` 动态创建类
- 理解 metaclass 的概念
- 用 metaclass 控制类的创建过程
- 了解 ORM 的基本原理

## 🤔 先想一个问题

普通代码用类来创建实例。那类本身是谁创建的？在 Python 里，创建类的东西叫**元类**（metaclass）。它就像「类的模具的模具」——你用模具做蛋糕，但谁来做模具呢？

带着这个问题，我们来看代码。

## 📖 看代码

```python
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
```

## 🔍 师兄给你逐行拆

> 代码已经在注释中做了详细说明，这里挑重点讲。

### 核心要点

- `type()` 有两个用法：查类型 和 动态创建类
- metaclass 最常见的应用是 ORM（对象关系映射）
- `__new__` 在 `__init__` 之前调用，控制对象的创建过程
- metaclass 是高级特性，日常开发很少需要自己写
- Django、SQLAlchemy 等框架底层大量使用 metaclass

## 🏃 跑一下试试

```bash
cd 39-metaclass
python metaclass.py
```

## 💡 师兄的碎碎念

- `type()` 有两个用法：查类型 和 动态创建类
- metaclass 最常见的应用是 ORM（对象关系映射）
- `__new__` 在 `__init__` 之前调用，控制对象的创建过程
- metaclass 是高级特性，日常开发很少需要自己写
- Django、SQLAlchemy 等框架底层大量使用 metaclass

## 🎓 这一关的知识点清单

| 知识点 | 说明 |
|--------|------|
| `type(name, bases, dict)` | 动态创建类 |
| `metaclass=XXX` | 指定元类 |
| `__new__` | 控制类/实例的创建过程 |
| `ORM` | 对象关系映射，用类操作数据库 |
| `Field / Model` | ORM 的基本组件 |

## ➡️ 下一关

下一关我们学习 [错误处理](../40-error-handling/README.md)，继续加油！
