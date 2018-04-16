# Kenten Danas, DATA 515, Homework 3

#Question 2

import unittest
from homework3 import create_dataframe


class HW3Test(unittest.TestCase):

	def test_rows(self):
		self.assertTrue(len(create_dataframe("class.db"))>10)

	def test_col_names(self):
		df = create_dataframe("class.db")
		self.assertTrue(set(create_dataframe("class.db").columns) == {'category_id', 'video_id', 'language'})

	def test_key(self):
		df = create_dataframe("class.db")
		self.assertTrue(len(df) == df.groupby(['video_id', 'language']).ngroups)

		#test if video_id and language are a key. This is expected to fail on class.db since for that data all three columns are needed for a possible key

	def test_path_exception(self):
		self.assertRaises(ValueError, create_dataframe, "unknown.db")

if __name__ == '__main__':
    unittest.main()