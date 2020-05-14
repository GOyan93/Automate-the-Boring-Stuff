"""
Automate the Boring Stuff
Title: Table Printer
Author: GOyan
Date: May 14, 2020
"""

table_data = [['apples', 'oranges', 'cherries', 'banana'], ['Alice', 'Bob', 'Carol', 'David'], ['dogs', 'cats', 'moose', 'goose']]

def print_table(list_data):
    length_list = []
    for item in list_data:
        longest_word = 0
        for word in item:
            if len(word) > longest_word:
                longest_word = len(word)
        length_list.append(longest_word)
    print(length_list)

print_table(table_data)
