# coding:utf-8
import re
# import sys
# reload(sys)
# sys.setdefaultencoding('utf-8')

a = "登录失败，请检查您的用户名或密码是否填写正确。"
b = a + "xxxxx"
print(b)
res = re.search(a, b, re.U| re.I | re.M)
print(res.group())