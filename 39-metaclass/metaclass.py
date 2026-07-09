# 元类（Metaclass）


print("=== 类也是对象 ===")


class Hello:
    def hello(self):
        return "Hello, world!"


# 类本身也是对象，默认由 type 创建。
print(type(Hello).__name__)  # type
print(type(Hello()).__name__)  # Hello
print(Hello().hello())  # Hello, world!


print("\n=== type() 动态创建类 ===")


def hello_func(self):
    return "Hello from dynamic class!"


# type(name, bases, attrs) 可以在运行时创建类。
Hello2 = type("Hello2", (object,), {"hello": hello_func})

obj = Hello2()
print(type(Hello2).__name__)  # type
print(type(obj).__name__)  # Hello2
print(obj.hello())  # Hello from dynamic class!


print("\n=== metaclass 控制类的创建 ===")


class AddMethodMeta(type):
    def __new__(mcls, name, bases, attrs):
        # 类创建前修改 attrs，相当于给类自动添加方法。
        attrs["add"] = lambda self, value: self.append(value)
        return super().__new__(mcls, name, bases, attrs)


class MyList(list, metaclass=AddMethodMeta):
    # metaclass 会接管 MyList 这个类的创建过程。
    pass


items = MyList([1, 2])
items.add(3)
print(items)  # [1, 2, 3]
print(type(MyList).__name__)  # AddMethodMeta


print("\n=== 简易 ORM：收集字段映射 ===")


class Field:
    def __init__(self, column_name, column_type):
        self.column_name = column_name
        self.column_type = column_type

    def __repr__(self):
        return f"{self.__class__.__name__}({self.column_name})"


class StringField(Field):
    def __init__(self, column_name):
        super().__init__(column_name, "varchar(100)")


class IntegerField(Field):
    def __init__(self, column_name):
        super().__init__(column_name, "bigint")


class ModelMeta(type):
    def __new__(mcls, name, bases, attrs):
        if name == "Model":
            # 基类 Model 本身不需要映射数据库表。
            return super().__new__(mcls, name, bases, attrs)

        mappings = {}
        for attr_name, attr_value in list(attrs.items()):
            if isinstance(attr_value, Field):
                # 找出类属性里的字段定义，收集成映射表。
                mappings[attr_name] = attr_value
                # 删除字段属性，避免和实例数据访问冲突。
                attrs.pop(attr_name)

        # 把 ORM 需要的元信息挂到类上。
        attrs["__mappings__"] = mappings
        attrs["__table__"] = name.lower()
        return super().__new__(mcls, name, bases, attrs)


class Model(dict, metaclass=ModelMeta):
    def __getattr__(self, key):
        try:
            # 允许 user.name 读取底层字典里的 user["name"]。
            return self[key]
        except KeyError as exc:
            raise AttributeError(key) from exc

    def __setattr__(self, key, value):
        # 允许 user.name = "Alice" 写入底层字典。
        self[key] = value

    def save_sql(self):
        fields = []
        values = []
        for attr_name, field in self.__mappings__.items():
            # 根据字段映射生成一条演示用 INSERT 语句。
            fields.append(field.column_name)
            values.append(repr(getattr(self, attr_name, None)))
        return f"INSERT INTO {self.__table__} ({', '.join(fields)}) VALUES ({', '.join(values)})"


class User(Model):
    id = IntegerField("id")
    name = StringField("username")
    email = StringField("email")


print(User.__table__)  # user
print(User.__mappings__)  # {'id': IntegerField(id), 'name': StringField(username), 'email': StringField(email)}

user = User(id=1, name="Alice", email="alice@example.com")
print(user.name)  # Alice
print(user.save_sql())  # INSERT INTO user (id, username, email) VALUES (1, 'Alice', 'alice@example.com')
