import unittest

from calculator import Count

class TestSub(unittest.TestCase):

	def setUp(self):
		print("Test Case Start")

	def tearDown(self):
		print("test Case end")

	def test_sub(self):
		j = Count(2, 3)
		self.assertEqual(j.sub(), -1)

	def test_sub2(self):
		j = Count(41, 76)
		self.assertEqual(j.sub(), -35)

if __name__ == '__main__':
	unittest.main()