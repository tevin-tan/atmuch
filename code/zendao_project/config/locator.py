# coding:utf-8

'''
    1. 全局变量定义
    2. WEB元素定位
'''
authentication = dict(
	name="admin",
	password="123456",
	# login url
	login_url="http://127.0.0.1:81/zentao/user-login.html",
)

locate = dict(

	# 用户名控件定位
	username=".//*[@id='account']",
	# 密码控件定位
	password=".//*[@id='login-form']/form/table/tbody/tr[2]/td/input",
	# 登录控件定位
	login_button=".//*[@id='submit']",

	new_project=".//*[@id='projectbox']/div[2]/a[1]",  # 创建项目
	menuproject=".//*[@id='menuproject']",  # 项目tab
	search_project_button=".//*[@id='currentItem']/span",  # 查找项目
	search_project_list=".//*[@id='search']",
	search_project_result=".//*[@id='searchResult']/div/ul/li/a",
	submenucreate=".//*[@id='submenucreate']",  # 添加项目
	delete_project=".//*[@id='taskTree']/div/div/div[2]/div/a[2]",  # 删除项目
	logout=".//*[@id='topnav']/a[1]",  # 退出登录

	pro_name=".//*[@id='name']",  # 项目名称
	pro_code=".//*[@id='code']",  # 项目代号
	date_start=".//*[@id='begin']",  # 起始日期
	date_end=".//*[@id='end']",  # 截止日期
	AWD=".//*[@id='days']",  # 可用工作日
	team_name=".//*[@id='team']",  # 团队名称

	# Todo list table(import)
	pro_type=".//*[@id='type']",  # 项目类型
	sprint="//option[@value='sprint']",  # 短期项目
	waterfall="//option[@value='waterfall']",  # 长期项目
	ops="//option[@value='ops']",  # 运维项目

	pro_des=".//*[@id='dataform']/table/tbody/tr[8]/td/div/div[2]/iframe",  # 项目描述

	# checkbutton  （#访问控制）
	access_default=".//*[@id='aclopen']",  # 默认设置
	access_private=".//*[@id='aclprivate']",  # 私有设置
	access_wihte_name=".//*[@id='aclcustom']",  # 自定义白名单
	save=".//*[@id='submit']",  # 保存
)
