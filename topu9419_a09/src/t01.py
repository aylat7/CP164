"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Ayla Topuz
ID:      169069419
Email:   topu9419@mylaurier.ca
__updated__ = "2024-03-20"
-------------------------------------------------------
"""
# Imports
from functions import insert_words, comparison_total
from Hash_Set_array import Hash_Set

print("Using array-based list Hash_Set")

fv = open('otoos610.txt', 'r')
hs = Hash_Set(20)

insert_words(fv, hs)
total, max_word = comparison_total(hs)

print("\nTotal Comparisons: {:,}".format(total))
print("Word with max comparisons: '{}': {:,}".format(max_word.word, max_word.comparisons))