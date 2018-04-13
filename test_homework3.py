# Kenten Danas, DATA 515, Homework 3

import unittest
from homework3 import create_dataframe


class HW3Test(unittest.TestCase):

	def test_rows(self):
		self.assertTrue(len(create_dataframe("class.db"))>10)

	def test_col_names(self):
		self.assertTrue(len(create_dataframe("class.db").columns)==3 and 
			'category_id' in create_dataframe("class.db").columns and 
			'video_id' in create_dataframe("class.db").columns and 
			'language' in create_dataframe("class.db").columns)

	def test_key(self):
		self.assertTrue(len(create_dataframe("class.db")) == create_dataframe("class.db").groupby(['video_id', 'language', 'category_id']).ngroups)

	def test_path_exception(self):
		self.assertRaises(ValueError, create_dataframe, "unknown.db")

if __name__ == '__main__':
    unittest.main()