# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 15:23:57 2020

@author: Xiaofan Hu
"""

input_list1 = [1,8,6,2,5,4,8,3,7]

def container_most_water(input_list):
    width = 0
    height = 0
    vol = 0
    n = -1
    m = -1
    
    for i in range(len(input_list)):
        for j in range(len(input_list)-1):
            
            width = j-i+1
            if input_list[i] > input_list[j+1]:
                height = input_list[j+1]
            else:
                height = input_list[i]
                
            vol_temp = width * height
            
            if vol < vol_temp:
                vol = vol_temp
                n = i
                m = j+1
                
    return vol

output = container_most_water(input_list1)
print(output)