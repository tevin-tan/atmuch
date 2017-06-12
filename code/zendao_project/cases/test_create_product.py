# coding:utf-8

import time
import unittest
from  common.page import Login
from common import model
from config.locator import PO_locate
from selenium.common import exceptions as EC


class Create_product(unittest.TestCase):
	'''产品测试'''

	def setUp(self):
		print("case start")
		self.page = Login()
		self.params = self.init_params()

	def init_params(self):
		params = dict(
			name="ZoneDirector",
			code="odc-001",
			des=" This is product descriptions!",
		)
		return params

	def tearDown(self):
		self.page.quit()
		print("case end")

	def click_action(self, locate, how="xpath"):
		try:
			if self.page.is_element_present(how, locate):
				self.page.driver.find_element_by_xpath(locate).click()
		except EC.NoSuchElementException as e:
			raise e

	def sendkey_action(self, locate, name, how="xpath"):
		if self.page.is_element_present(how, locate):
			self.page.driver.find_element_by_xpath(locate).send_keys(name)

	def delete_product_is_exist(self, name):
		'''删除已经存在同名的产品'''
		time.sleep(1)
		self.click_action(PO_locate["product"])
		time.sleep(1)
		self.click_action(PO_locate["currentItem"])
		time.sleep(1)
		self.sendkey_action(PO_locate["serachItem"], name)
		time.sleep(1)

		if self.page.is_element_present("xpath", PO_locate["Item"]):
			e3 = self.page.driver.find_element_by_xpath(PO_locate["Item"])  # 匹配结果
			print(e3.text)
			if e3.text == name:  # 判断是否找到项目
				self.click_action(PO_locate["all_product"])
				for i in range(10):
					xpath = ".//*[@id='productTableList']/tr[" + str(i) + "]/td[2]/a"
					print xpath
					if self.page.is_element_present("xpath", xpath):
						if self.page.driver.find_element_by_xpath(xpath).text == name:  # 查找产品
							self.click_action(xpath)  # 点击产品名称
							if self.click_action(PO_locate["delete_product"]):  # 点击删除
								if self.page.is_alert_present():
									print("点击确认, 删除!")
									time.sleep(1)
									res = self.page.close_alert_and_get_its_text()
									model.logger_init().info("res:" + res)
									break
						else:
							continue
		else:
			print("not found %s" % (PO_locate["Item"]))

	def test_delete_product_02(self):
		'''删除产品'''
		self.delete_product_is_exist(self.params["name"])

	def test_create_product_01(self):
		'''创建产品'''

		# 判断该产品是否已经存在，如果存在则先删除。
		self.delete_product_is_exist(self.params["name"])

		# Product
		time.sleep(2)
		self.click_action(PO_locate["product"])
		time.sleep(1)
		self.page.driver.find_element_by_xpath(".//*[@id='submenucreate']").click()
		time.sleep(1)
		# Product name
		self.sendkey_action(PO_locate["name"], self.params["name"])
		# product code
		self.sendkey_action(PO_locate["code"], self.params["code"])
		# product owner
		self.click_action(PO_locate["PO_chosen"])
		time.sleep(1)
		# select owner
		self.click_action(PO_locate["PO_owner"])
		time.sleep(1)
		# Test owner
		self.click_action(PO_locate["QD_chosen"])
		# select test owner
		self.click_action(PO_locate["test_owner"])
		# public owner
		self.click_action(PO_locate["RD_chosen"])
		# select public owner
		self.click_action(PO_locate["select_RD_chosen"])
		# product discription
		self.sendkey_action(PO_locate["product_des"], self.params["des"])
		# check access control
		self.click_action(PO_locate["access_private"])
		# save
		self.click_action(PO_locate["save"])


if __name__ == '__main__':
	Create_product()
