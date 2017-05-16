# coding:utf-8

import unittest


class MyTest(unittest.TestCase):
	def setUp(self):
		pass

	def tearDown(self):
		pass

	@unittest.skip("直接跳过测试")
	def test_skip(self):
		print("跳过这个case")

	@unittest.skipIf(3 > 2, "当条件为真时跳过测试")
	def test_skip_if(self):
		print("条件满足则执行")

	@unittest.skipUnless(3 > 2, "当条件为True时执行测试")
	def test_skip_unless(self):
		print("除非条件满足才执行")

	@unittest.expectedFailure
	def test_expected_failure(self):
		self.assertEqual(2, 3)


if __name__ == '__main__':
	unittest.main()
