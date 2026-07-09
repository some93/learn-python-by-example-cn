# 第 39 关：元类（师兄带你学 Python）

## 🎯 这一关你会学到

- 类本身也是对象
- `type()` 不只用来查看类型，也能动态创建类
- metaclass 如何控制“类的创建过程”
- `__new__()` 在创建对象时扮演什么角色
- ORM 为什么常用 metaclass 收集字段定义

## 🤔 先想一个问题

实例是类创建出来的。比如：

```python
user = User()
```

那类本身是谁创建出来的？

在 Python 里，类也是对象。创建类的“模具”默认是 `type`。如果你想控制类是怎么被创建的，就会用到元类，也就是 metaclass。

元类可以理解成：**类的类**。

## 📖 看代码

```python
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
```

## 🔍 师兄给你逐行拆

### 类也是对象

```python
class Hello:
    def hello(self):
        return "Hello, world!"


print(type(Hello).__name__)
print(type(Hello()).__name__)
```

**这行在干嘛？**

`Hello()` 创建实例，实例的类型是 `Hello`。

但 `Hello` 这个类本身也有类型，它的类型是 `type`。

也就是说：

```python
Hello 是 type 创建出来的对象
Hello() 是 Hello 创建出来的对象
```

这就是理解元类的入口。

---

### `type()` 动态创建类

```python
Hello2 = type("Hello2", (object,), {"hello": hello_func})
```

**这行在干嘛？**

`type()` 有三参数用法，可以动态创建类：

```python
type(类名, 父类元组, 属性方法字典)
```

这里创建了一个类 `Hello2`，继承自 `object`，并拥有一个 `hello` 方法。

**为什么平时不这么写？**

普通业务代码用 `class` 语法更清楚。`type()` 动态创建类主要用于框架、代码生成、插件系统等高级场景。

---

### metaclass：拦截类创建过程

```python
class AddMethodMeta(type):
    def __new__(mcls, name, bases, attrs):
        attrs["add"] = lambda self, value: self.append(value)
        return super().__new__(mcls, name, bases, attrs)
```

**这行在干嘛？**

`AddMethodMeta` 继承自 `type`，所以它是一个元类。

当某个类声明：

```python
class MyList(list, metaclass=AddMethodMeta):
    pass
```

Python 创建 `MyList` 这个类时，会调用 `AddMethodMeta.__new__()`。

我们在 `attrs` 里塞入一个 `add` 方法，所以 `MyList` 自动拥有了 `add()`。

**`__new__` 是什么？**

`__new__` 负责创建对象，发生在 `__init__` 之前。

这里创建的对象不是普通实例，而是“类对象”本身。

---

### ORM 为什么会用 metaclass？

```python
class User(Model):
    id = IntegerField("id")
    name = StringField("username")
    email = StringField("email")
```

**这行在干嘛？**

你写的是一个 Python 类，但它其实也在描述数据库表：

- 类名 `User` -> 表名 `user`
- 属性 `id` -> 数据库列 `id`
- 属性 `name` -> 数据库列 `username`
- 属性 `email` -> 数据库列 `email`

metaclass 可以在 `User` 类创建时扫描这些 `Field`，收集成 `__mappings__`。

---

### `ModelMeta` 收集字段

```python
for attr_name, attr_value in list(attrs.items()):
    if isinstance(attr_value, Field):
        mappings[attr_name] = attr_value
        attrs.pop(attr_name)
```

**这行在干嘛？**

`attrs` 是类定义里的属性字典。`ModelMeta` 会找出所有 `Field` 对象，放进 `mappings`。

然后把这些字段从类属性里移除，避免它们和实例属性冲突。

最后给类加上：

```python
__mappings__
__table__
```

这些就是 ORM 后续生成 SQL 的元数据。

---

### 生成 SQL

```python
user = User(id=1, name="Alice", email="alice@example.com")
print(user.save_sql())
```

**这行在干嘛？**

`User` 继承自 `dict`，所以可以保存键值数据。`__getattr__` 和 `__setattr__` 让你可以用属性方式访问字典内容：

```python
user.name
```

`save_sql()` 根据 `__mappings__` 和实例数据拼出一条 SQL：

```sql
INSERT INTO user (id, username, email) VALUES (1, 'Alice', 'alice@example.com')
```

**现实提醒**

这只是教学版 ORM。真实项目不能这样拼 SQL，要用参数化查询，避免 SQL 注入。

## 🏃 跑一下试试

```bash
$ python metaclass.py
=== 类也是对象 ===
type
Hello
Hello, world!

=== type() 动态创建类 ===
type
Hello2
Hello from dynamic class!

=== metaclass 控制类的创建 ===
[1, 2, 3]
AddMethodMeta

=== 简易 ORM：收集字段映射 ===
user
{'id': IntegerField(id), 'name': StringField(username), 'email': StringField(email)}
Alice
INSERT INTO user (id, username, email) VALUES (1, 'Alice', 'alice@example.com')
```

## 💡 师兄的碎碎念

- 类也是对象；普通类默认由 `type` 创建。
- `type(name, bases, attrs)` 可以动态创建类。
- metaclass 是创建类的类，可以拦截和修改类创建过程。
- `__new__` 负责创建对象，`__init__` 负责初始化对象。
- 元类是高级特性，日常业务代码很少需要自己写；更多出现在 ORM、框架、声明式 API 里。

## 🎓 这一关的知识点清单

- **type()**：一参数时查看类型，三参数时动态创建类。
- **metaclass**：创建类对象的类。
- **__new__()**：控制对象创建过程，早于 `__init__()`。
- **attrs**：类定义阶段收集到的属性字典。
- **ORM**：对象关系映射，把类和数据库表结构联系起来。
- **元数据**：像 `__mappings__`、`__table__` 这样描述类结构的数据。

## ➡️ 下一关

面向对象进阶到这里收尾。下一关进入错误处理：程序出错时如何捕获异常、恢复流程、留下清楚的错误信息 👉 [下一关：错误处理 →](../40-error-handling/)




