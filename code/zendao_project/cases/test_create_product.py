# coding:utf-8

import time
import unittest
from  common.page import Login
from common import model
from config.locator import PO_locate
from selenium.common import exceptions as EC
import datetime
import random


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
			time.sleep(1)
			self.page.driver.find_element_by_xpath(locate).clear()
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

	def _serach_product(self, name):
		'''搜索产品'''
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
				e3.click()
				model.logger_init().info(u"产品已被找到")
				return True
			else:
				model.logger_init().ERROR(u"该产品未添加")
				return False
		else:
			print("not found %s" % (PO_locate["Item"]))

	def _create_product(self):

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
		model.logger_init().info(u'产品创建成功')

	def test_02_delete_product(self):
		'''删除产品'''
		self.delete_product_is_exist(self.params["name"])

	def test_01_create_product(self):
		'''创建产品'''
		self._create_product()

	def test_03_select_product(self):
		'''查找产品'''
		name = "ZoneDirector"
		self._serach_product(name)

	'''
		step:
			1. 查找产品"ZoneDirector"，如果查到则创建产品计划
			2. 名称为”交换设备“, 产品计划开始日期为2017-01-01, 结束日期2017-02-01，选择测试阶段为一星期
			3. 填写产品描述，并执行保存
	'''

	def test_04_create_product_plan(self):
		'''创建产品计划'''
		conf = dict(
			po_plan=".//*[@id='submenuplan']",
			cre_plan=".//*[@id='titlebar']/div[2]/a",
			name=".//*[@id='title']",
			start=".//*[@id='begin']",
			end=".//*[@id='end']",
			check=".//*[@id='dataform']/table/tbody/tr[4]/td[2]/label[1]",
			des=".//*[@id='dataform']/table/tbody/tr[5]/td/div/div[2]/iframe",  # 项目描述
			save=".//*[@id='submit']"
		)

		data = dict(
			po_name="ZoneDirector",
			name=u"交换设备",
			s_t="2017-01-01",
			e_t="2017-02-01",
			description=u"产品计划，要求一星期内完成"
		)

		def _create_plan(conf, data):
			self.click_action(conf['po_plan'])
			self.click_action(conf['cre_plan'])
			self.sendkey_action(conf['name'], data["name"])

			self.sendkey_action(conf['start'], data['s_t'])
			self.sendkey_action(conf['end'], data['e_t'])
			self.click_action(conf['check'])
			# self.sendkey_action(conf['des'], data['description'])
			if self.page.is_element_present("xpath", conf["des"]):
				self.page.driver.find_element_by_xpath(conf["des"]).send_keys(data['description'])
			self.click_action(conf['save'])
			model.logger_init().info(u"产品计划已经创建成功")

		# step 1
		if self._serach_product(data["po_name"]):  # 查找产品
			_create_plan(conf, data)  # 创建计划
		else:
			self._create_product()  # 创建产品
			_create_plan(conf, data)  # 创建计划

	'''
		设置产品计划周期为1星期
	'''

	def test_05_create_product_palan_use_period(self):
		'''产品计划设置周期'''
		'''创建产品计划'''
		conf = dict(
			po_plan=".//*[@id='submenuplan']",
			cre_plan=".//*[@id='titlebar']/div[2]/a",
			name=".//*[@id='title']",
			start=".//*[@id='begin']",
			end=".//*[@id='end']",
			check=".//*[@id='dataform']/table/tbody/tr[4]/td[2]/label[1]",
			des=".//*[@id='dataform']/table/tbody/tr[5]/td/div/div[2]/iframe",  # 项目描述
			save=".//*[@id='submit']"
		)

		data = dict(
			po_name="ZoneDirector",
			name=u"交换设备",
			s_t="2017-01-01",
			e_t="2017-02-01",
			description=u"产品计划，要求一星期内完成"
		)

		def _set_time(conf, data):
			self.click_action(conf['po_plan'])
			self.click_action(conf['cre_plan'])
			# step 3
			self.sendkey_action(conf['name'], data["name"] + str(random.randrange(1000)))

			self.sendkey_action(conf['start'], data['s_t'])
			self.sendkey_action(conf['end'], data['e_t'])
			self.click_action(conf['check'])
			res = self.page.driver.find_element_by_xpath(conf['end']).get_attribute('value')
			print("res:" + res)
			d1 = datetime.datetime.strptime(data["s_t"], '%Y-%m-%d')
			d2 = datetime.datetime.strptime(res, '%Y-%m-%d')
			delt = d2 - d1
			print(delt)
			if delt.days == 7:
				model.logger_init().info(u'计划周期设置为一星期')

			if self.page.is_element_present("xpath", conf["des"]):
				self.page.driver.find_element_by_xpath(conf["des"]).send_keys(data['description'])
			self.click_action(conf['save'])
			model.logger_init().info(u"产品计划已经创建成功")

		if self._serach_product(data["po_name"]):  # 查找产品
			_set_time(conf, data)  # 创建计划
		else:
			self._create_product()  # 创建产品
			_set_time(conf, data)  # 创建计划

	'''
		创建发布
	'''

	def test_06_create_product_publish(self):
		'''创建产品发布'''

		conf = dict(
			relase=".//*[@id='submenurelease']",
			cre_publish=".//*[@id='titlebar']/div[2]/a",
			select_version=".//*[@id='build_chosen']/a",
			name=".//*[@id='name']",
			date=".//*[@id='date']",
			des=".//*[@id='dataform']/table/tbody/tr[4]/td/div/div[2]/iframe",
			fileBox=".//*[@id='fileBox1']/tbody/tr/td[1]/div/input",
			save=".//*[@id='submit']",
		)

		data = dict(
			po_name="ZoneDirector",
			name="ZD",
			version="1001",
			date="2017-01-30",
			description=u"发布产品测试验证",
			file="D:\\ui.rar",

		)

		if self._serach_product(data["po_name"]):  # 查找产品
			self.click_action(conf['relase'])
			self.click_action(conf['cre_publish'])
			self.sendkey_action(conf['name'], data['name'])
			if self.page.is_element_present("xpath", conf['select_version']):
				self.page.driver.find_element_by_xpath(conf['select_version']).send_keys(data['version'])
			self.sendkey_action(conf['date'], data['date'])
			if self.page.is_element_present("xpath", conf['des']):
				self.page.driver.find_element_by_xpath(conf['des']).send_keys(data['description'])
			if self.page.is_element_present("xpath", conf["fileBox"]):
				self.page.driver.find_element_by_xpath(conf["fileBox"]).send_keys(data['file'])
			self.click_action(conf['save'])
			model.logger_init().info(u"产品发布成功")

		else:
			self._create_product()  # 创建产品
			self.click_action(conf['relase'])
			self.click_action(conf['cre_publish'])
			self.sendkey_action(conf['name'], data['name'])
			if self.page.is_element_present("xpath", conf['select_version']):
				self.page.driver.find_element_by_xpath(conf['select_version']).send_keys(data['version'])
			self.sendkey_action(conf['date'], data['date'])
			if self.page.is_element_present("xpath", conf['des']):
				self.page.driver.find_element_by_xpath(conf['des']).send_keys(data['description'])
			if self.page.is_element_present("xpath", conf["fileBox"]):
				self.page.driver.find_element_by_xpath(conf["fileBox"]).send_keys(data['file'])
			self.click_action(conf['save'])
			model.logger_init().info(u"产品发布成功")


if __name__ == '__main__':
	Create_product()
