# coding:utf-8
import unittest
import os
import time
from HTMLTestRunner import HTMLTestRunner

# 定义测试用例的目录为当前目录
t_dir = os.path.dirname(os.getcwd())
print("t_dir %s :" % t_dir)
# test_dir = '../project_test/'
test_dir = t_dir

discover = unittest.defaultTestLoader.discover(test_dir, pattern='test*.py')


# ======查找测试报告目录，找到最新生成的测试报告文件==========
def new_report(testreport):
	lists = os.listdir(testreport)
	lists.sort(key=lambda fn: os.path.getmtime(testreport + "\\" + fn))
	file_new = os.path.join(testreport, lists[-1])
	print(file_new)
	return file_new


if __name__ == '__main__':
	# 按照一定格式获取当前时间
	now = time.strftime("%Y-%m-%d %H_%M_%S")

	# 定义报告存放路径
	local_dir = os.path.dirname(os.getcwd())
	print("local_dir:", local_dir)
	path = local_dir + "\\log\\" + now + "result.html"
	print("path:", path)
	fp = open(path, 'wb')

	# 定义测试报告
	runner = HTMLTestRunner(stream=fp,
	                        title='测试报告',
	                        description='用例执行情况:')

	runner.run(discover)
	fp.close()  # 关闭测试报告
	test_report = "D:\workspace\Selenium2\chapter_07\project_test\log"
	new_report = new_report(test_report)
