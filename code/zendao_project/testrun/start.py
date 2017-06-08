# coding:utf-8
import unittest
from cases import zendaologin

suite = unittest.TestSuite()
# 构造测试套件
suite.addTest(zendaologin.TestLogin('test_login_success'))
suite.addTest(zendaologin.TestLogin('test_login_error_name'))

if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(suite)
