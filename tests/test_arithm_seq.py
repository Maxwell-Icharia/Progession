import unittest
from main.arithm_seq import arith

class Arithmetic(unittest.TestCase):
	def test_is_list(self):
		self.assertTrue([98], list)
	def test_not_empty_list(self):	
		self.assertFalse([], list)



if __name__ == '__main__':
	unittest.main()