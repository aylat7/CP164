"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Ayla Topuz
ID:      169069419
Email:   topu9419@mylaurier.ca
__updated__ = "2024-02-09"
-------------------------------------------------------
"""
from List_array import List
from Food_utilities import read_food
from Food import Food

food_list = List()

file = open("foods.txt", "r")
for line in file:
    food = read_food(line)
    food_list.append(food)
    
print(f"append: {[str(food) for food in food_list]}\n")

print(f"__eq__ method: {food_list == food_list}\n")

print(f"__getitem__ method: {food_list[0]}\n")

food_list.append(Food("Lasagna", 7, False, 135))
food_list.clean()
print(f"clean  method: {[str(food) for food in food_list]}\n")

test_list1 = List()
test_list1.append(Food("Lasagna", 7, False, 135))
test_list2 = List()
test_list2.append(Food("Butter Chicken", 2, False, 490))
test_list3 = List()
test_list3.append(Food("BBQ Pork", 1, False, 920))
print(f"combine method: {[str(food) for food in food_list]}\n")

test_list1 = List()
test_list1.append(Food("Lasagna", 7, False, 135))
test_list1.append(Food("Butter Chicken", 2, False, 490))
test_list2 = List()
test_list2.append(Food("Butter Chicken", 2, False, 490))
test_list2.append(Food("BBQ Pork", 1, False, 920))
food_list.intersection(test_list1, test_list2)
print(f"intersection method: {[str(food) for food in food_list]}\n")

food_list.prepend(Food("Lasagna", 7, False, 135))
print(f"prepend method: {[str(food) for food in food_list]}\n")

food_list.remove_front()
print(f"remove front method: {[str(food) for food in food_list]}\n")

food_list.remove_many(Food("Beef with Green Pepper", 1, False, 251))
print(f"remove many method: {[str(food) for food in food_list]}\n")

food_list1, food_list2 = food_list.split()
print(f"split method: 1: {[str(food) for food in food_list1]} 2: {[str(food) for food in food_list2]}]n")

food_list1, food_list2 = food_list.split_alt()
print(f"split alt method: 1: {[str(food) for food in food_list1]} 2: {[str(food) for food in food_list2]}]n")

test_list1 = List()
test_list1.append(Food("Lasagna", 7, False, 135))
test_list2 = List()
test_list2.append(Food("Butter Chicken", 2, False, 490))
food_list.union(test_list1, test_list2)
print(f"combine method: {[str(food) for food in food_list]}\n")

print("done")





