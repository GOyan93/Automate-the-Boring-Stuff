"""
Automate the Boring Stuff
Title: Table Printer
Author: GOyan
Date: May 14, 2020
"""

table_data = [['apples', 'oranges', 'cherries', 'banana'], ['Alice', 'Bob', 'Carol', 'David'], ['dogs', 'cats', 'moose', 'goose']]

def print_table(list_data):
    length_list = []
    reordered_data = []
    for item in list_data:
        longest_word = 0
        for word in item:
            if len(word) > longest_word:
                longest_word = len(word)
        length_list.append(longest_word)
    for x in range(len(list_data[0])):
	    for y in range(len(list_data)):
		    print(list_data[y][x].rjust(length_list[y]), end = ' ')    
	    print('')
        
    
print_table(table_data)
