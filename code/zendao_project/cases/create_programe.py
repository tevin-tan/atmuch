# coding:utf-8

import unittest

class Create_program(unittest.TestCase):
	u'''创建项目'''

	def setUp(self):
		print("---create program case test start-----")

	def tearDown(self):
		print("---create program case test end-----")

	def test_create_program_01(self):
		u'''创建一个项目'''
		print(u'创建项目')
