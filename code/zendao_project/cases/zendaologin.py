# coding:utf-8

from selenium import webdriver
import logging
from config.locatar import locate, authentication
import unittest
import time
import os
import datetime
import traceback
from common import model
import sys
import re
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import NoSuchElementException
import selenium.common.exceptions  as EC

reload(sys)
sys.setdefaultencoding('utf-8')


class TestLogin(unittest.TestCase):
	'''测试登录用例'''

	def setUp(self):
		print("Test Case Start")
		self.log = model.logger_init()

		self.driver = model.browser()
		self.driver.implicitly_wait(30)
		self.base_url = "http://127.0.0.1:81"
		self.accept_next_alert = True
		self.error_text = u'登录失败，请检查您的用户名或密码是否填写正确。'

	def tearDown(self):
		self.driver.quit()
		print("-------------test Case end----------------\n\n")

	def open(self, url):
		'''打开特定Url'''
		self.driver.get(url)

	def type_username(self, loc, name):
		'''输入用户名'''
		try:
			self.driver.find_element_by_xpath(loc).clear()
			self.driver.find_element_by_xpath(loc).send_keys(name)
			return True
		except NoSuchElementException as e:
			print(e)
			return False

	def type_password(self, loc, password):
		'''输入密码'''
		self.driver.find_element_by_xpath(loc).clear()
		self.driver.find_element_by_xpath(loc).send_keys(password)

	def type_submit(self, loc):
		self.driver.find_element_by_xpath(loc).click()

	# def skipTest(self, reason):
	# 	"""Skip this test."""
	# 	raise self.skipTest(reason)

	def is_login_sucess(self):
		u'''判断是否获取到登录账户名称'''
		try:
			c_url = self.driver.current_url
			if c_url == "http://127.0.0.1:81/zentao/my.html":
				return True
		except:
			return False

	# case 1: login success!
	def test_login_01_success(self):
		'''用户名密码正确登录成功'''
		self.open(self.base_url + "/zentao/user-login-L3plbnRhby9teS5odG1s.html")
		# try:
		self.type_username(locate["username"], authentication["name"])
		self.type_password(locate["password"], authentication["password"])
		self.type_submit(locate["login_button"])
		print(self.driver.title)

		time.sleep(3)
		# 判断结果
		result = self.is_login_sucess()
		self.assertTrue(result)
		if result:
			print(u'[TestCase]登录成功, 用例执行成功')
		else:
			print(u'[TestCase]用例执行失败')

	def get_alert_present(self):
		'''获取登录弹窗登录错误提示'''
		if self.is_alert_present():
			print("A popup window")
			# 关闭弹窗，获取错误信息
			alert_text = self.close_alert_and_get_its_text()
			print("登录失败错误提示信息:" + alert_text)
			self.assertIn(self.error_text, alert_text, "(%s) not found in (%s)" % (self.error_text, alert_text))

	# case 2: login with error name or password
	def test_login_02_error_name(self):
		'''用户名错误，登录失败'''
		browser = self.driver
		self.open(self.base_url + "/zentao/user-login-L3plbnRhby9teS5odG1s.html")
		self.type_username(locate["username"], "tan")
		self.type_password(locate["password"], authentication["password"])
		self.type_submit(locate["login_button"])
		print(browser.title)
		time.sleep(2)
		browser.get_screenshot_as_file("a.jpg")
		model.insert_img(browser, "name_error.jpg")

		# 校验弹窗
		self.get_alert_present()
		# 判断结果
		result = self.is_login_sucess()
		self.assertFalse(result)
		if not result:
			print(u'[TestCase]登录失败，用例执行成功')
		else:
			print(u'[TestCase]用例执行失败')

		'''
		# 切换到ifram弹窗
		browser.switch_to.frame("hiddenwin")
		alert = browser.switch_to.alert
		alert_text = alert.text
		print("alert_text:" + alert_text)
		time.sleep(2)
		self.writeLog(browser)
		alert.accept() 
		'''

		# 字符串查找
		'''
		if alert_text.find(u'登录失败，请检查您的用户名或密码是否填写正确。') != -1:
			self.log.info("登录失败，用户名错误, case run pass")
		else:
			logging.error("登录失败，用户名错误, case run error")
		'''

		# 直接字符串比对
		'''
		if alert_text == "登录失败，请检查您的用户名或密码是否填写正确。":
			print("登录失败，校验成功")
		else:
			print("校验失败") 
		'''

		# 利用正则表达式匹配
		'''
		rs = re.search(u'登录失败，请检查您的用户名或密码是否填写正确。', alert_text)
		# print(rs.group())
		if rs.group() != None:
			self.log.info("case run pass")
		else:
			self.log.ERROR("case run error")
		'''

	def test_login_03_error_password(self):
		'''密码错误，登录失败'''
		browser = self.driver
		self.open(self.base_url + "/zentao/user-login-L3plbnRhby9teS5odG1s.html")
		# try:
		self.type_username(locate["username"], authentication["name"])
		self.type_password(locate["password"], "11111")
		self.type_submit(locate["login_button"])
		print(browser.title)
		browser.get_screenshot_as_file("a.jpg")
		model.insert_img(browser, "password_error.jpg")

		if self.is_alert_present():
			print("have alert ok")
			alert_text = self.close_alert_and_get_its_text()
			print("alert_text:" + alert_text)
			# assert (alert_text == "登录失败，请检查您的用户名或密码是否填写正确。" )
			if alert_text == "登录失败，请检查您的用户名或密码是否填写正确。":
				print("登录失败，校验成功 case run pass")
			else:
				print("校验失败 case run failed")
				raise ValueError("校验失败 case run failed")
		else:
			print("not found alert present!")
		# except Exception as e:
		#     logging.error(e)
		#     return False

	def test_login_04_name_empty(self):
		'''用户名为空，登录失败'''
		browser = self.driver
		self.open(self.base_url + "/zentao/user-login-L3plbnRhby9teS5odG1s.html")
		try:
			self.type_username(locate["username"], "")
			self.type_password(locate["password"], authentication["password"])
			self.type_submit(locate["login_button"])
			print(browser.title)
			model.insert_img(browser, "name_empty.jpg")

			if self.is_alert_present():
				print("have alert ok")
				alert_text = self.close_alert_and_get_its_text()
				print("alert_text:" + alert_text)
				if alert_text == "登录失败，请检查您的用户名或密码是否填写正确。":
					print("登录失败，校验成功 case run pass")
				else:
					print("校验失败 case run failed")
			else:
				print("not found alert present!")

		except Exception as e:
			logging.error(e)

	def test_login_05_password_empty(self):
		'''密码为空，登录失败'''
		browser = self.driver
		self.open(self.base_url + "/zentao/user-login-L3plbnRhby9teS5odG1s.html")
		self.type_username(locate["username"], authentication["name"])
		self.type_password(locate["password"], "")
		self.type_submit(locate["login_button"])
		print(browser.title)
		model.insert_img(browser, "password_empty.jpg")

		# 切换到ifram弹窗
		browser.switch_to.frame("hiddenwin")
		alert = browser.switch_to.alert
		alert_text = alert.text
		print("alert_text:" + alert_text)
		time.sleep(2)
		# self.writeLog(browser)
		alert.accept()

		if alert_text == "登录失败，请检查您的用户名或密码是否填写正确。":
			print("登录失败，校验成功")
		else:
			print("校验失败")
			raise ValueError("密码为空，登录失败")

	def test_login_06_many_times(self):
		'''连续登录3次'''
		self.skipTest("not run")  # Todo 跳过这个用例
		self.open(self.base_url + "/zentao/user-login-L3plbnRhby9teS5odG1s.html")
		for i in range(3):
			self.type_username(locate["username"], authentication["name"])
			self.type_password(locate["password"], "")
			self.type_submit(locate["login_button"])
		print(self.driver.title)
		time.sleep(2)
		model.insert_img(self.driver, "many_times_error.jpg")

		if self.is_alert_present():
			print("have alert ok")
			alert_text = self.close_alert_and_get_its_text()
			print("alert_text:" + alert_text)

			if alert_text.find(u'您还有3次尝试机会。') != -1:
				self.log.info("登录失败，用户名错误, case run pass")
			else:
				raise ValueError("登录失败，用户名错误, case run error")
		else:
			print("not found alert present!")

	def writeLog(self, driver):
		# 组合日志文件名（当前文件名+当前时间）.比如：case_login_success_20150817192533
		basename = os.path.splitext(os.path.basename(__file__))[0]
		logFile = basename + "-" + datetime.datetime.now().strftime("%Y%m%d%H%M%S") + ".log"
		logging.basicConfig(filename=logFile)
		s = traceback.format_exc()
		logging.error(s)
		print(basename, logFile)

	# time.sleep(1)
	# driver.get_screenshot_as_file("./" + datetime.datetime.now().strftime("%Y%m%d%H%M%S") + "-screenshot_error.jpg")

	def is_alert_present(self):
		'''
			校验是否有alert出现
		:return: true / false
		'''
		try:
			self.driver.switch_to_alert()
		except NoAlertPresentException as e:
			print(e)
			return False
		return True

	def close_alert_and_get_its_text(self):
		'''关闭alert, 获取alert 文本信息'''
		try:
			alert = self.driver.switch_to_alert()
			alert_text = alert.text
			if self.accept_next_alert:
				alert.accept()
			else:
				alert.dismiss()
			return alert_text
		finally:
			self.accept_next_alert = True


if __name__ == '__main__':
	unittest.main()
