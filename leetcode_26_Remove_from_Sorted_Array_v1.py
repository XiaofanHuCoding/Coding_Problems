# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 21:31:17 2020

@author: Xiaofan Hu
"""

input_list1 = [1, 1, 2]
input_list2 = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
input_list3 = [0, 0, 0, 0, 0, 1, 1, 1, 1, 1 ,1, 1, 1, 1, 1, 1, 2, 2, 3, 4, 6, 7, 8, 8, 8, 9, 10, 11]


def remove_duplicates(input_list):
    pointer = 0
    
    if len(input_list) == 0:
        return 0
    else:
        list_val = input_list[0]
        for val in input_list:
            if val != list_val:
                pointer += 1
                list_val = val
                input_list[pointer] = val
        output_list = input_list[0:pointer+1]
            
    return pointer+1, output_list, input_list
            

output1, output_list1, input_list1 = remove_duplicates(input_list1)
output2, output_list2, input_list2 = remove_duplicates(input_list2)
output3, output_list3, input_list3 = remove_duplicates(input_list3)

print(output1)
print(output_list1)
print(input_list1)
print('\n')
print(output2)
print(output_list2)
print(input_list2)
print('\n')
print(output3)
print(output_list3)
print(input_list3)
