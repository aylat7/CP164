"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Ayla Topuz
ID:      169069419
Email:   topu9419@mylaurier.ca
__updated__ = "2024-01-12"
-------------------------------------------------------
"""

from Food_utilities import write_foods, read_foods

with open("foods.txt", "r") as file:
    foods_list = read_foods(file)

for food in foods_list:
    print(food.name, food.origin, food.is_vegetarian, food.calories)

with open("new_foods.txt", "w", encoding="utf-8") as newFile:
    
    write_foods(newFile, foods_list)
