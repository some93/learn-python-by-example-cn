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
