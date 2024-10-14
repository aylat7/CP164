"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Ayla Topuz
ID:      169069419
Email:   topu9419@mylaurier.ca
__updated__ = "2024-03-14"
-------------------------------------------------------
"""
from functions import hash_table 
from Food_utilities import read_foods

fh = open('foods.txt', 'r')
foods = read_foods(fh)
hash_table(7, foods)