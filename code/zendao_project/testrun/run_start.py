# coding:utf-8
import unittest
import sys

import cases
from cases import test_create_programe
from cases import test_zendaologin
from cases import test_create_product
from HTMLTestRunner import HTMLTestRunner
import os
import time

reload(sys)
sys.setdefaultencoding('utf-8')


class RunTestSuite(object):
	def __init__(self):
		pass

	def Add_test_case_run(self):
		# 创建项目测试用例添加到测试套
		'''方法三'''
		suite1 = unittest.TestLoader().loadTestsFromTestCase(cases.test_zendaologin.TestLogin)
		suite2 = unittest.TestLoader().loadTestsFromTestCase(cases.test_create_programe.Create_program)
		suite3 = unittest.TestLoader().loadTestsFromTestCase(cases.test_create_product.Create_product)
		test_suite = [suite1, suite2, suite3]
		suite = unittest.TestSuite(test_suite)

		return suite

	def Add_test_case_run_02(self):
		suite = unittest.TestSuite()

		'''方法二'''
		# 登录测试用例添加到测试套
		test_login = [
			test_zendaologin.TestLogin('test_login_01_success'),
			test_zendaologin.TestLogin('test_login_02_error_name'),
			test_zendaologin.TestLogin('test_login_03_error_password'),
			test_zendaologin.TestLogin('test_login_04_name_empty'),
			test_zendaologin.TestLogin('test_login_05_password_empty'),
			test_zendaologin.TestLogin('test_login_06_many_times')
		]
		suite.addTests(test_login)

		test_create_program = [test_create_programe.Create_program('test_create_program_01')]
		suite.addTests(test_create_program)

		return suite

	def Add_test_case_run_03(self):
		suite = unittest.TestSuite()
		'''方法一'''
		# 构造测试套件，添加测试用例
		suite.addTest(test_zendaologin.TestLogin('test_login_01_success'))
		suite.addTest(test_zendaologin.TestLogin('test_login_02_error_name'))
		suite.addTest(test_zendaologin.TestLogin('test_login_03_error_password'))
		suite.addTest(test_zendaologin.TestLogin('test_login_04_name_empty'))
		suite.addTest(test_zendaologin.TestLogin('test_login_05_password_empty'))
		suite.addTest(test_zendaologin.TestLogin('test_login_06_many_times'))
		return suite

	def set_reporter_path(self):
		# 定义报告存放路径以及格式
		local_dir = os.path.dirname(os.getcwd())
		print("local_dir %s :" % local_dir)
		path = local_dir + "\\log\\" + now + "-result.html"
		print("path:", path)
		return local_dir, path

	def new_report(self, testreport):
		# ======查找测试报告目录，找到最新生成的测试报告文件==========
		lists = os.listdir(testreport)
		lists.sort(key=lambda fn: os.path.getmtime(testreport + "\\" + fn))
		file_new = os.path.join(testreport, lists[-1])
		print(file_new)
		return file_new


if __name__ == "__main__":
	RT = RunTestSuite()
	ST = RT.Add_test_case_run()
	# runner = unittest.TextTestRunner()
	# unittest.TextTestRunner(verbosity=1)
	# 按照一定格式获取当前时间
	now = time.strftime("%Y-%m-%d %H_%M_%S")
	PT = RT.set_reporter_path()
	print("path:", PT)
	fp = open(PT[1], 'wb')

	# 定义测试报告
	runner = HTMLTestRunner(stream=fp, title='测试报告', description='用例执行情况:')

	runner.run(ST)
	fp.close()  # 关闭测试报告
	# test_report = "D:\CODE_ALL\\auto_zendao_test\zendao_login\log"
	# new_report = RT.new_report(test_report)
	new_report = RT.new_report(PT[0])
