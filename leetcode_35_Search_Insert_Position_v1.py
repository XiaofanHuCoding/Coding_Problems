# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 11:05:26 2020

@author: Xiaofan Hu
"""

input_list1 = [1,3,5,6]
target_val1 = 5

input_list2 = [1,3,5,6]
target_val2 = 2

input_list3 = [1,3,5,6]
target_val3 = 7

input_list4 = [1,3,5,6]
target_val4 = 0

def search_insert(input_list, target_val):
    j = 0
    
    for i in range(len(input_list)):
        if input_list[i] == target_val:
            j = i
            output_list = input_list
        else:
            if input_list[0] > target_val:
                output_list = [target_val] + input_list
                j = 0
            elif input_list[-1] < target_val:
                output_list = input_list + [target_val]
                j = len(input_list)
            elif (input_list[i] > target_val) and (input_list[i-1] < target_val):
                first_list = input_list[0:i]
                second_list = input_list[i:len(input_list)]
                output_list = first_list + [target_val] + second_list
                j = i
            
    return j, output_list

n1, output_list1 = search_insert(input_list1, target_val1)
n2, output_list2 = search_insert(input_list2, target_val2)
n3, output_list3 = search_insert(input_list3, target_val3)
n4, output_list4 = search_insert(input_list4, target_val4)

print(n1)
print(output_list1)
print('\n')
print(n2)
print(output_list2)
print('\n')
print(n3)
print(output_list3)
print('\n')
print(n4)
print(output_list4)