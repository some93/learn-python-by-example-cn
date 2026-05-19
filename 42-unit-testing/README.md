# 第 42 关：单元测试（师兄带你学 Python）

## 🎯 这一关你会学到

- 理解单元测试的意义
- 用 `unittest` 编写测试
- 掌握常用断言方法
- 使用 `setUp` / `tearDown`

## 🤔 先想一个问题

你写了一个函数，手动试了几次感觉没问题。三个月后改了一行代码，结果之前能跑的功能全挂了。如果当初写了**单元测试**，改完代码跑一下测试就知道有没有破坏东西。

带着这个问题，我们来看代码。

## 📖 看代码

```python
# 单元测试

import unittest

# 被测试的代码
class Dict(dict):
    """支持属性访问的字典"""
    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(f"'Dict' 没有属性 '{key}'")

    def __setattr__(self, key, value):
        self[key] = value

# 测试类
class TestDict(unittest.TestCase):
    # setUp：每个测试方法前执行
    def setUp(self):
        self.d = Dict(a=1, b=2)

    # tearDown：每个测试方法后执行
    def tearDown(self):
        pass

    # 测试方法必须以 test_ 开头
    def test_init(self):
        d = Dict(a=1, b='test')
        self.assertEqual(d.a, 1)
        self.assertEqual(d.b, 'test')
        self.assertTrue(isinstance(d, dict))

    def test_key(self):
        self.assertEqual(self.d['a'], 1)

    def test_attr(self):
        self.assertEqual(self.d.a, 1)

    def test_keyerror(self):
        with self.assertRaises(KeyError):
            _ = self.d['empty']

    def test_attrerror(self):
        with self.assertRaises(AttributeError):
            _ = self.d.empty

    def test_setattr(self):
        self.d.c = 3
        self.assertEqual(self.d.c, 3)
        self.assertEqual(self.d['c'], 3)

# 常用断言方法
# assertEqual(a, b)      a == b
# assertNotEqual(a, b)   a != b
# assertTrue(x)          bool(x) is True
# assertFalse(x)         bool(x) is False
# assertRaises(Error)    抛出指定异常
# assertIn(a, b)         a in b
# assertIsNone(x)        x is None

if __name__ == '__main__':
    unittest.main()

# 运行测试的方式：
# python unit-testing.py
# python -m unittest unit-testing
# python -m pytest（需安装 pytest）
```

## 🔍 师兄给你逐行拆

> 代码已经在注释中做了详细说明，这里挑重点讲。

### 核心要点

- 测试类继承 `unittest.TestCase`，测试方法以 `test_` 开头
- `setUp` 在每个测试方法前执行，用来准备测试数据
- `assertRaises` 用 `with` 语句检查异常
- 运行测试：`python -m unittest` 或 `python -m pytest`
- 好的测试应该：独立、可重复、覆盖边界情况

## 🏃 跑一下试试

```bash
cd 42-unit-testing
python unit-testing.py
```

## 💡 师兄的碎碎念

- 测试类继承 `unittest.TestCase`，测试方法以 `test_` 开头
- `setUp` 在每个测试方法前执行，用来准备测试数据
- `assertRaises` 用 `with` 语句检查异常
- 运行测试：`python -m unittest` 或 `python -m pytest`
- 好的测试应该：独立、可重复、覆盖边界情况

## 🎓 这一关的知识点清单

| 知识点 | 说明 |
|--------|------|
| `unittest.TestCase` | 测试类的基类 |
| `test_xxx 方法` | 以 test_ 开头的方法是测试用例 |
| `assertEqual(a, b)` | 断言 a == b |
| `assertRaises(Error)` | 断言抛出指定异常 |
| `setUp / tearDown` | 测试前后的初始化和清理 |

## ➡️ 下一关

下一关我们学习 [文件读写](../43-file-io/README.md)，继续加油！
