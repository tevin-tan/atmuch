# coding:utf-8

'''
    1. 全局变量定义
    2. WEB元素定位
'''
authentication = dict(
	name="admin",
	password="123456"
)

locate = dict(

	# login url
	login_url="http://127.0.0.1:81/zentao/user-login-L3plbnRhby9teS5odG1s.html",
	# 用户名控件定位
	username=".//*[@id='account']",
	# 密码控件定位
	password=".//*[@id='login-form']/form/table/tbody/tr[2]/td/input",
	# 登录控件定位
	login_button=".//*[@id='submit']",

)
