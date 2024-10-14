"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Ayla Topuz
ID:      169069419
Email:   topu9419@mylaurier.ca
__updated__ = "2024-01-08"
-------------------------------------------------------
"""
# Imports

from functions import matrix_stats

a = [[2, 0, -2, 1], [10, 4, -5, 9], [-6, 3, 6, 0]]

small, large, total, average = matrix_stats(a)

print(f"{small, large, total, average}")