# 第 42 关：单元测试

## 🎯 这一关你会学到

- 单元测试解决什么问题
- 如何用 `unittest.TestCase` 编写测试类
- 测试方法为什么要以 `test_` 开头
- 常用断言：`assertEqual`、`assertIn`、`assertRaises`
- `setUp()` / `tearDown()` 如何准备和清理测试数据

## 🤔 先想一个问题

你写了一个函数，手动试了几次，感觉没问题。

三个月后你改了一行代码，结果老功能悄悄坏了。你可能根本不知道，直到用户来报 bug。

单元测试就是给代码装自动报警器：每次改完跑一遍，哪里坏了立刻告诉你。

## 📖 看代码

```python
# 单元测试

import unittest


class AttrDict(dict):
    """支持属性访问的字典。"""

    def __getattr__(self, key):
        try:
            # 让 data.a 等价于 data["a"]。
            return self[key]
        except KeyError as exc:
            # 属性访问失败时应该抛 AttributeError，而不是 KeyError。
            raise AttributeError(f"'AttrDict' 没有属性 '{key}'") from exc

    def __setattr__(self, key, value):
        # 让 data.a = 1 等价于 data["a"] = 1。
        self[key] = value


class TestAttrDict(unittest.TestCase):
    def setUp(self):
        # 每个测试方法执行前都会重新准备一份数据。
        self.data = AttrDict(a=1, b="test")

    def tearDown(self):
        # 每个测试方法执行后都会清理，避免测试之间互相影响。
        self.data.clear()

    def test_init(self):
        self.assertEqual(self.data.a, 1)
        self.assertEqual(self.data.b, "test")
        self.assertIsInstance(self.data, dict)

    def test_key_access(self):
        self.assertEqual(self.data["a"], 1)
        self.assertIn("b", self.data)

    def test_attr_access(self):
        self.assertEqual(self.data.a, 1)

    def test_setattr(self):
        self.data.c = 3
        self.assertEqual(self.data.c, 3)
        self.assertEqual(self.data["c"], 3)

    def test_key_error(self):
        # assertRaises 用来验证代码确实抛出了预期异常。
        with self.assertRaises(KeyError):
            _ = self.data["missing"]

    def test_attr_error(self):
        with self.assertRaises(AttributeError):
            _ = self.data.missing


if __name__ == "__main__":
    # verbosity=2 会显示每个测试方法的名字和结果。
    unittest.main(verbosity=2)
```

## 🔍 师兄给你逐行拆

### 被测试代码：`AttrDict`

```python
class AttrDict(dict):
    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError as exc:
            raise AttributeError(f"'AttrDict' 没有属性 '{key}'") from exc

    def __setattr__(self, key, value):
        self[key] = value
```

**这行在干嘛？**

`AttrDict` 继承自 `dict`，但支持属性访问：

```python
d = AttrDict(a=1)
d.a      # 1
d["a"]   # 1
```

访问不存在的属性时，把 `KeyError` 转成 `AttributeError`，更符合属性访问的语义。

---

### 测试类必须继承 `unittest.TestCase`

```python
class TestAttrDict(unittest.TestCase):
```

**这行在干嘛？**

`unittest.TestCase` 提供了大量断言方法和测试运行机制。测试类继承它，Python 才知道这是测试。

**为什么类名通常以 Test 开头？**

不是硬性要求，但这是惯例。读代码的人一眼知道这是测试类。

---

### `setUp()` 和 `tearDown()`

```python
def setUp(self):
    self.data = AttrDict(a=1, b="test")

def tearDown(self):
    self.data.clear()
```

**这行在干嘛？**

`setUp()` 会在每个测试方法执行前运行，用来准备测试数据。

`tearDown()` 会在每个测试方法执行后运行，用来清理资源。

**重点**

每个测试方法都会拿到一份新的 `self.data`。测试之间应该互相独立，不要依赖执行顺序。

---

### 测试方法以 `test_` 开头

```python
def test_init(self):
    self.assertEqual(self.data.a, 1)
    self.assertEqual(self.data.b, "test")
    self.assertIsInstance(self.data, dict)
```

**这行在干嘛？**

`unittest` 默认只会自动发现以 `test_` 开头的方法。

这里测试三件事：

- 属性访问 `self.data.a` 正常；
- 字符串值正常；
- `AttrDict` 仍然是 `dict` 的实例。

---

### 常用断言

```python
self.assertEqual(self.data["a"], 1)
self.assertIn("b", self.data)
self.assertIsInstance(self.data, dict)
```

**这行在干嘛？**

断言就是“我期望这里必须成立”。

常用断言：

- `assertEqual(a, b)`：断言 `a == b`
- `assertNotEqual(a, b)`：断言 `a != b`
- `assertTrue(x)`：断言 `bool(x) is True`
- `assertFalse(x)`：断言 `bool(x) is False`
- `assertIn(a, b)`：断言 `a in b`
- `assertIsNone(x)`：断言 `x is None`
- `assertIsInstance(obj, cls)`：断言对象是某类型实例

---

### 测试异常：`assertRaises`

```python
def test_key_error(self):
    with self.assertRaises(KeyError):
        _ = self.data["missing"]

def test_attr_error(self):
    with self.assertRaises(AttributeError):
        _ = self.data.missing
```

**这行在干嘛？**

有些代码正确行为就是“应该抛异常”。比如访问不存在的 key 应该抛 `KeyError`，访问不存在的属性应该抛 `AttributeError`。

`assertRaises` 可以测试这类行为。

**容易踩的坑**

不要只测试“正常输入”。边界条件、错误输入、异常路径也要测。

---

### 运行测试

```python
if __name__ == "__main__":
    unittest.main(verbosity=2)
```

**这行在干嘛？**

直接运行文件时，启动 unittest 测试 runner。`verbosity=2` 会显示每个测试方法的名字，更适合教程观察。

也可以在项目根目录运行：

```bash
python -m unittest 42-unit-testing/unit-testing.py
```

## 🏃 跑一下试试

```bash
$ python unit-testing.py
test_attr_access (__main__.TestAttrDict.test_attr_access) ... ok
test_attr_error (__main__.TestAttrDict.test_attr_error) ... ok
test_init (__main__.TestAttrDict.test_init) ... ok
test_key_access (__main__.TestAttrDict.test_key_access) ... ok
test_key_error (__main__.TestAttrDict.test_key_error) ... ok
test_setattr (__main__.TestAttrDict.test_setattr) ... ok

----------------------------------------------------------------------
Ran 6 tests in 0.000s

OK
```

## 💡 师兄的碎碎念

- 测试方法必须以 `test_` 开头，否则默认不会被 unittest 发现。
- 测试应该独立、可重复，不依赖其他测试先运行。
- `setUp()` 每个测试前执行，适合准备数据；`tearDown()` 每个测试后执行，适合清理资源。
- 好测试不只测正常路径，也测异常和边界条件。
- `pytest` 更流行、更简洁，但 `unittest` 是标准库，自带、稳定、适合入门。

## 🎓 这一关的知识点清单

- **unittest**：Python 标准库测试框架。
- **TestCase**：测试类基类，提供断言和运行机制。
- **test_ 方法**：会被测试 runner 自动发现。
- **assertEqual/assertIn/assertRaises**：常用断言方法。
- **setUp/tearDown**：测试前准备和测试后清理。
- **测试独立性**：测试之间不共享状态，不依赖顺序。

## ➡️ 下一关

测试会保护代码行为。下一关看文件读写：程序如何把数据写到磁盘，再从磁盘读回来 👉 [下一关：文件读写 →](../43-file-io/)


