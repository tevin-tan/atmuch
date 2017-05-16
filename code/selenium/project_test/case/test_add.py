import unittest

from calculator import Count

class TestAdd(unittest.TestCase):

	def setUp(self):
		print("Test Case Start")

	def tearDown(self):
		print("test Case end")

	def test_add(self):
		j = Count(2, 3)
		self.assertEqual(j.add(), 5)

	def test_add2(self):
		j = Count(41, 76)
		self.assertEqual(j.add(), 117)

if __name__ == '__main__':
	unittest.main()

