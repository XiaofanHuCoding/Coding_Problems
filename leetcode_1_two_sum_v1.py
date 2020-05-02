# -*- coding: utf-8 -*-
"""
Created on Sun Apr 26 08:17:30 2020

@author: Xiaofan Hu
"""

# First try

input_list1 = [2, 7, 11, 15, 17, 23, 90, 4, 10]
target1 = 14

def two_sum(input_list, target):
    for i in range(len(input_list)):
        for j in range(len(input_list)):
            if j == i:
                pass
            else:
                if input_list[i] + input_list[j] == target:
                    print('Find, i =', i, 'and', 'j =', j)
                    return [i, j]

output_list = two_sum(input_list1, target1)
print(output_list)