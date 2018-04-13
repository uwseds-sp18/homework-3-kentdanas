# Kenten Danas, DATA 515, Homework 3

# Question 1

def create_dataframe(path):
	import pandas as pd
	import sqlite3
	import os

	if not os.path.exists(path):
		raise ValueError("File path is not valid. Try again.")

	conn = sqlite3.connect(path)
	youtube = pd.read_sql_query("""SELECT DISTINCT video_id, category_id, 'us' as language FROM USvideos 
									UNION 
									SELECT DISTINCT video_id, category_id, 'ca' as language FROM CAvideos 
									UNION 
									SELECT DISTINCT video_id, category_id, 'gb' as language FROM GBvideos 
									UNION 
									SELECT DISTINCT video_id, category_id, 'fr' as language FROM FRvideos 
									UNION 
									SELECT DISTINCT video_id, category_id, 'de' as language FROM DEvideos;""", conn)
	return youtube
    	

