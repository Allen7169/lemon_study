import unittest
from kangaiduo_case import TestLoginMethod

suite = unittest.TestSuite()

loader = unittest.TestLoader()
suite.addTest(loader.loadTestsFromTestCase(TestLoginMethod))

runner = unittest.TextTestRunner()
runner.run(suite)
