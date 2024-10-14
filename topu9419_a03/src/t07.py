"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Ayla Topuz
ID:      169069419
Email:   topu9419@mylaurier.ca
__updated__ = "2024-01-25"
-------------------------------------------------------
"""
# Imports
from functions import stack_maze

maze = {'Start': ['A', 'B'], 'A': [], 'B': ['C'], 'C': ['D'], 'D': ['X', 'B']}

path = stack_maze(maze)

print("maze", path)