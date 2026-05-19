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
