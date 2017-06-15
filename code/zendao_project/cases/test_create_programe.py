# coding:utf-8

import unittest
from common.page import Login
from config import locator
import time
from selenium.common import exceptions as EC
from common import model


class Create_program(unittest.TestCase):
	u'''项目测试'''

	def init_parameters(self):
		conf = {
			'pro_name': '9.14_zonedirector_test',
			'pro_code': 'odc-0007',
			'date_start': '2015-11-14',
			'date_end': '2015-11-30',
			'available_work_days': '16',
			'team_name': 'automation',
			'pro_type': 'ops',
			'pro_des': "hello automation, congratulation to your",
			'pro_access': 'access_private',
		}
		return conf

	def setUp(self):
		# 打开浏览器
		self.config = self.init_parameters()
		self.lg = Login()
		print("---create program case test start-----")

	def tearDown(self):
		# close self.lg.driver
		time.sleep(2)
		self.lg.quit()
		print("---create program case test end-----")

	def delete_project_if_exist(self, name):
		'''删除已经存在同名的项目'''
		time.sleep(1)
		el = self.lg.driver.find_element_by_xpath(locator.locate["menuproject"])
		el.click()
		time.sleep(2)
		e1 = self.lg.driver.find_element_by_xpath(locator.locate["search_project_button"])  # 搜索下拉按钮
		e1.click()
		time.sleep(1)
		e2 = self.lg.driver.find_element_by_xpath(locator.locate["search_project_list"])  # 输入搜索文本
		e2.send_keys(name)
		time.sleep(1)
		if self.lg.is_element_present("xpath", locator.locate["search_project_result"]):
			e3 = self.lg.driver.find_element_by_xpath(locator.locate["search_project_result"])  # 匹配结果
			if e3.text == name:  # 判断是否找到项目
				self.lg.driver.find_element_by_xpath(locator.locate["delete_project"]).click()  # 删除项目
				if self.lg.is_alert_present():
					print("点击确认!")
					time.sleep(2)
					res = self.lg.close_alert_and_get_its_text()
					model.logger_init().info("res:" + res)
			else:
				print("not found element!")

	'''
		Case01: test_01_create_program
		name: 创建项目
		step:
			1. 创建项目，项目名称为9.14_zonedirector_test
			2. 查看项目是否已经存在，如果存在则先删除
			3. 项目代号为"odc-0007", 起始日期：2015-11-14， 截止日期：2015-11-30， 可用工作日：16， 项目团队：automation，项目类型为：运维项目，
			访问控制为：私人项目
			4. 保存项目
			5. 查看项目是否创建成功
	'''

	def test_01_create_program(self):
		u'''创建一个私有，维护项目，并删除项目'''
		print(u'创建项目')

		prj_name = self.config['pro_name']
		prj_code = self.config['pro_code']
		date_start = self.config['date_start']
		date_end = self.config['date_end']
		awd = self.config['available_work_days']
		team_name = self.config['team_name']
		prj_type = self.config['pro_type']
		prj_des = self.config['pro_des']
		prj_access = self.config['pro_access']

		self.delete_project_if_exist(prj_name)  # 查找当前项目是否已经存在，若存在则先删除，再创建
		self.lg.driver.refresh()
		# step 1 切换项目页
		self.select_project()
		# step 2 输入项目名称
		time.sleep(1)
		self.type_project_name(prj_name)
		# step 3  输入项目的code
		time.sleep(1)
		self.type_project_code(prj_code)
		# step 4  输入起始及截止日期
		time.sleep(1)
		self.type_date(date_start, date_end)
		# step 5    输入可用工作日
		time.sleep(1)
		self.type_available_day(awd)
		# step 6  输入团队名称
		time.sleep(1)
		self.type_team_name(team_name)
		# step 7 选择项目类型
		time.sleep(1)
		self.select_project_type(prj_type)
		# step 8 填写项目描述
		time.sleep(1)
		self.type_project_description(prj_des)
		# step 9 选择访问类型
		time.sleep(1)
		self.select_access_option(prj_access)
		# step 10 保存项目
		time.sleep(1)
		self.save_project()

	# # 创建项目
	# self.create_an_project(prj_name, prj_code, date_start, date_end, awd, team_name, prj_type, prj_des, prj_access)

	'''
		Case2: test_02_create_program
		name: 创建创建一个默认，短期项目, 并关联产品
		step:
			1. 创建项目，项目名称为9.14_zonedirector_test
			2. 查看项目是否已经存在，如果存在则先删除
			3. 项目代号为"odc-0007", 起始日期：2015-11-14， 截止日期：2015-11-30， 可用工作日：16， 项目团队：automation，项目类型为：运维项目，
			访问控制为：私人项目
			4. 保存项目
			5. 查看项目是否创建成功
	'''

	def test_02_create_program(self):
		u'''创建一个默认，短期项目, 关联产品'''
		product_name = "ZoneDirector"
		conf = {
			'pro_name': '9.17_zonedirector_test',
			'pro_code': 'odc-0003',
			'date_start': '2015-11-14',
			'date_end': '2015-11-30',
			'available_work_days': '16',
			'team_name': 'automation',
			'pro_type': 'sprint',
			'pro_des': "hello automation, congratulation to your",
			'pro_access': 'access_private',
		}

		prj_name = conf['pro_name']
		prj_code = conf['pro_code']
		date_start = conf['date_start']
		date_end = conf['date_end']
		awd = conf['available_work_days']
		team_name = conf['team_name']
		prj_type = conf['pro_type']
		prj_des = conf['pro_des']
		prj_access = conf['pro_access']

		self.delete_project_if_exist(prj_name)  # 查找当前项目是否已经存在，若存在则先删除，再创建
		self.lg.driver.refresh()
		# step 1 切换项目页
		self.select_project()
		# step 2 输入项目名称
		time.sleep(1)
		self.type_project_name(prj_name)
		# step 3  输入项目的code
		time.sleep(1)
		self.type_project_code(prj_code)
		# step 4  输入起始及截止日期
		time.sleep(1)
		self.type_date(date_start, date_end)
		# step 5    输入可用工作日
		time.sleep(1)
		self.type_available_day(awd)
		# step 6  输入团队名称
		time.sleep(1)
		self.type_team_name(team_name)
		# step 7 选择项目类型
		time.sleep(1)
		self.select_project_type(prj_type)
		# step 8 填写项目描述
		time.sleep(1)
		self.type_project_description(prj_des)
		# step 9 选择访问类型
		time.sleep(1)
		self.select_access_option(prj_access)

		# 关联产品
		# import pdb
		# pdb.set_trace()
		if self.lg.is_element_present("xpath", ".//*[@id='products_chosen']/ul"):
			el = self.lg.driver.find_element_by_xpath(".//*[@id='products_chosen']/ul")
			el.click()
			time.sleep(1)
			el.send_keys(product_name)
			time.sleep(1)
			for i in range(1, 10):
				xp = ".//*[@id='products_chosen']/div/ul/li[" + str(i) + "]"
				if self.lg.is_element_present("xpath", xp):
					if self.lg.driver.find_element_by_xpath(xp).text == product_name:
						time.sleep(1)
						self.lg.driver.find_element_by_xpath(xp).click()
						break
				else:
					continue
		else:
			print("not found", u'关联产品')

		# step 10 保存项目
		time.sleep(1)
		self.save_project()

	'''
		Case: test_03_show_project
		caseName: 查看所有项目
		CaseStep:
			1. 点击项目页
			2. 找到所有项目按钮，点击所有项目
			3. 查看并展示项目列表
	'''

	def test_03_show_project(self):
		'''查看所有项目'''
		conf = dict(
			submenuall=".//*[@id='submenuall']",
			project=".//*[@id='menuproject']",
		)

		# def is_element_action(xpath, how="xpath"):
		# 	'''确认“所有项目”元素是否可见'''
		# 	try:
		# 		self.lg.is_element_present(how, xpath)  # 所有项目
		# 		time.sleep(1)
		# 		self.lg.driver.find_element_by_xpath(xpath).click()
		# 		return True
		# 	except EC.NoSuchElementException as e:
		# 		raise e

		self.is_element_action(conf['project'])  # step 1
		self.is_element_action(conf["submenuall"])  # step 2

		# step 3
		for i in range(1, 100):
			xpath = ".//*[@id='projectTableList']/tr[" + str(i) + "]/td[2]/a"
			# print xpath
			time.sleep(1)
			if self.lg.is_element_present("xpath", xpath):
				el = self.lg.driver.find_element_by_xpath(xpath).text
				if el == "":
					break
				else:
					print(u"项目" + el)
					continue
			else:
				break

	def is_element_action(self, xpath, how="xpath"):
		'''确认“所有项目”元素是否可见'''
		try:
			self.lg.is_element_present(how, xpath)  # 所有项目
			time.sleep(1)
			self.lg.driver.find_element_by_xpath(xpath).click()
			return True
		except EC.NoSuchElementException as e:
			raise e

	def select_project(self):
		'''切换到创建项目页面'''
		try:
			time.sleep(1)
			element = self.lg.driver.find_element_by_xpath(locator.locate['new_project'])
			element.click()
		except EC.NoSuchElementException, e:
			print(e)
			try:
				el = self.lg.driver.find_element_by_xpath(locator.locate["menuproject"])
				el.click()
				time.sleep(1)
				element = self.lg.driver.find_element_by_xpath(locator.locate["submenucreate"])
				time.sleep(1)
				element.click()
			except EC.NoSuchElementException, e:
				print(e)
				raise e

	def type_project_name(self, project_name):
		'''输入项目名称'''
		try:
			pn = self.lg.driver.find_element_by_xpath(locator.locate['pro_name'])  # 项目名称
			pn.send_keys(project_name)
		except EC.NoSuchElementException, e:
			print(e)
			raise e

	def type_project_code(self, project_code):
		'''输入项目代号'''
		try:
			b1 = self.lg.driver.find_element_by_xpath(locator.locate['pro_code'])  # 项目名称
			b1.send_keys(project_code)
		except EC.NoSuchElementException, e:
			print(e)
			raise e

	def type_date(self, data_start, date_end):
		'''
			选择日历，日期
		'''
		d_s = self.lg.driver.find_element_by_xpath(locator.locate['date_start'])  # 起始日期
		d_s.clear()
		d_s.send_keys(data_start)
		d_s.click()
		d_e = self.lg.driver.find_element_by_xpath(locator.locate["date_end"])  # 结束日期
		d_e.clear()
		d_e.send_keys(date_end)
		d_e.click()

	def type_available_day(self, available_work_days):
		'''
		输入可用工作日
		:param available_work_days:
		:return:
		'''
		return self.lg.driver.find_element_by_xpath(locator.locate['AWD']).send_keys(available_work_days)  # 可用工作日

	def type_team_name(self, team_name):
		'''
		输入团队名称
		:param team_name:
		:return:
		'''
		return self.lg.driver.find_element_by_xpath(locator.locate['team_name']).send_keys(team_name)  # 团队名称

	def select_project_type(self, project_type="sprint"):
		'''
		项目类型（短期，长期，维护）, 默认为sprint
		:param project_type:
		:return:
		'''
		p_t = self.lg.driver.find_element_by_xpath(locator.locate["pro_type"])  # 找到列表
		p_t.find_element_by_xpath(locator.locate[project_type]).click()

	def type_project_description(self, project_description):
		'''项目描述'''
		return self.lg.driver.find_element_by_xpath(locator.locate['pro_des']).send_keys(project_description)

	def select_access_option(self, access='access_default'):
		'''
		选择访问控制类型，默认"access_default"
		:param access:
		:return:
		'''
		p_a = self.lg.driver.find_element_by_xpath(locator.locate[access])
		p_a.click()

	def save_project(self):
		# 保存创建项目
		self.lg.driver.find_element_by_xpath(locator.locate['save']).click()

	# -----------------------------------------------------------------------------------------------------------------------
	def create_an_project(
		self, p_n=None, p_c=None, d_st=None, d_end=None, awd=0, t_n=None, Pro_type='sprint',
		p_des=None,
		access='access_default'):

		# 切换到创建项目页面
		try:
			time.sleep(1)
			element = self.lg.driver.find_element_by_xpath(locator.locate['new_project'])
			element.click()
		except EC.NoSuchElementException, e:
			print(e)
			try:
				el = self.lg.driver.find_element_by_xpath(locator.locate["menuproject"])
				el.click()
				time.sleep(1)
				element = self.lg.driver.find_element_by_xpath(locator.locate["submenucreate"])
				time.sleep(1)
				element.click()
			except EC.NoSuchElementException, e:
				print(e)

		time.sleep(1)
		try:
			b1 = self.lg.driver.find_element_by_xpath(locator.locate['pro_name'])  # 项目名称
			b1.send_keys(p_n)
		except EC.NoSuchElementException, e:
			print(e)
		e_p_code = self.lg.driver.find_element_by_xpath(locator.locate['pro_code'])  # 项目代号
		e_p_code.send_keys(p_c)

		# 选择日历，日期
		d_s = self.lg.driver.find_element_by_xpath(locator.locate['date_start'])  # 起始日期
		d_s.clear()
		d_s.send_keys(d_st)
		d_s.click()
		d_e = self.lg.driver.find_element_by_xpath(locator.locate["date_end"])  # 结束日期
		d_e.clear()
		d_e.send_keys(d_end)
		d_e.click()

		self.lg.driver.find_element_by_xpath(locator.locate['AWD']).send_keys(awd)  # 可用工作日
		time.sleep(1)
		self.lg.driver.find_element_by_xpath(locator.locate['team_name']).send_keys(t_n)  # 团队名称

		# 下拉列表菜单
		p_t = self.lg.driver.find_element_by_xpath(locator.locate["pro_type"])  # 项目类型（短期，长期，维护）
		p_t.find_element_by_xpath(locator.locate[Pro_type]).click()
		time.sleep(1)

		# 文本描述
		self.lg.driver.find_element_by_xpath(locator.locate['pro_des']).send_keys(p_des)  # 项目描述

		# 访问模式选择，checkbutton
		p_a = self.lg.driver.find_element_by_xpath(locator.locate[access])
		p_a.click()
		time.sleep(1)

		# 保存，创建成功
		self.lg.driver.find_element_by_xpath(locator.locate['save']).click()


if __name__ == '__main__':
	Create_program()
