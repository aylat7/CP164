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

from functions import file_analyze

fv = open("task4file.txt", "r", encoding="utf-8")

print(file_analyze(fv))

fv.close()
