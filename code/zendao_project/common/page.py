# coding:utf-8
import model
from config.locator import locate, authentication
from selenium.common import exceptions as EC
import sys

reload(sys)
sys.setdefaultencoding("utf-8")


class Login(object):
	'''
		登录页面
	'''

	def __init__(self):
		self.url = "http://127.0.0.1:81/zentao/user-login.html"
		self.driver = model.browser()
		self.open()
		self.type_username(locate["username"], authentication["name"])
		self.type_password(locate["password"], authentication["password"])
		self.type_submit(locate["login_button"])
		self.accept_next_alert = True

	def open(self):
		'''打开特定Url'''
		self.driver.get(self.url)

	def type_username(self, loc, name):
		'''输入用户名'''
		try:
			self.driver.find_element_by_xpath(loc).clear()
			self.driver.find_element_by_xpath(loc).send_keys(name)
			return True
		except EC.NoSuchElementException as e:
			print(e)
			return False

	def type_password(self, loc, password):
		'''输入密码'''
		self.driver.find_element_by_xpath(loc).clear()
		self.driver.find_element_by_xpath(loc).send_keys(password)

	def type_submit(self, loc):
		self.driver.find_element_by_xpath(loc).click()

	def quit(self):
		self.driver.quit()

	def is_element_present(self, how, what):
		try:
			self.driver.find_element(by=how, value=what)
		except EC.NoSuchElementException as e:
			return False
		return True

	def is_alert_present(self):
		try:
			self.driver.switch_to_alert()
		except EC.NoAlertPresentException as e:
			return False
		return True

	def close_alert_and_get_its_text(self):
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
	lg = Login()
	lg.quit()
