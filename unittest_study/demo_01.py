import unittest
from unittest_study.math_method import MathMethod


class TestAddMethod(unittest.TestCase):  # 继承unittest里面的TestCase类，专门编写测试用例
    # 编写测试用例
    # 注意：
    # 一个用例是一个函数，不能传参，只有self关键字
    # 所有的用例（所有的函数都是test开头: test_）
    def test_add_two_positive(self):
        result = MathMethod(1, 1).add()
        print("test_add_two_positive的result为:", result)
        # 第一个参数和第二个参数，分别是预期结果和实际结果，进行比对，如果不匹配时会进行报错
        # 第三个参数在用例执行失败的时候才会抛出的信息
        try:
            self.assertEqual(3, result, "结果报错")
        except AssertionError as e:
            print("断言出错了")
            raise e

    def test_add_two_zero(self):
        result = MathMethod(0, 0).add()
        print("test_add_two_zero的result为:", result)
        self.assertEqual(0, result, "结果报错")

    def test_add_two_negative(self):
        result = MathMethod(-1, -2).add()
        print("test_add_two_negative的result为:", result)
        self.assertEqual(-3, result, "结果报错")


class TestMultiMethod(unittest.TestCase):  # 继承unittest里面的TestCase类，专门编写测试用例
    # 编写测试用例
    def test_multi_two_positive(self):
        result = MathMethod(1, 1).multi()
        print("test_multi_two_positive的result为:", result)
        self.assertEqual(1, result, "结果报错")

    def test_multi_two_zero(self):
        result = MathMethod(0, 0).multi()
        print("test_multi_two_zero的result为:", result)
        self.assertEqual(0, result, "结果报错")

    def test_multi_two_negative(self):
        result = MathMethod(-1, -2).multi()
        print("test_multi_two_negative的result为:", result)
        self.assertEqual(2, result, "结果报错")


if __name__ == '__main__':
    unittest.main()
    # 执行顺序按照ASCII编码
    # 所以执行结果 n p z


