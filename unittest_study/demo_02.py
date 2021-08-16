import unittest
from unittest_study.demo_01 import TestAddMethod, TestMultiMethod
import demo_01
suite = unittest.TestSuite()    # suite为存储用例的实例

# 添加用例方法一：
# suite.addTest(TestAddMethod("test_add_two_positive"))
# suite.addTest(TestAddMethod("test_add_two_zero"))


# 添加用例方法二：TestLoader
loader = unittest.TestLoader()    # 创建一个加载器
# 如果导入的是具体的类，loadTestsFromTestCase方法可以直接填写类名
# suite.addTest(loader.loadTestsFromTestCase(TestAddMethod))
# 如果导入的是模块，loadTestsFromModule方法可以直接填写模块名
suite.addTest(loader.loadTestsFromModule(demo_01))


# 原始的报告编写
# with open 是上下文管理器
with open("test.txt", "w", encoding="utf-8") as file:
    runner = unittest.TextTestRunner(stream=file, descriptions=True, verbosity=2)
    runner.run(suite)

