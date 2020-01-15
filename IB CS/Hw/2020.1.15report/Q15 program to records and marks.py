#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 15 08:21:12 2020

@author: hhshhd
"""
# program to store class records and marks.

limit = 4
values = [20,6,38,50,40]
flag = True
for counter1 in range(limit-1):
    minimum = counter1
    
    for counter2 in range(counter1+1,limit):
        if values[counter2] < values[minimum]:
            minimum = counter2
    if minimum != counter1:
        temporary = values[minimum]
        values[minimum] = values[counter1]
        values[counter1] = temporary


while flag == True:
    flag = False
    for counter in range(limit-1):
        if values[counter] > values[counter+1]:
            temporary = values[counter]
            values[counter] = values[counter+1]
            values[counter+1] = temporary
            flag = True

for i in range(limit):
    print(values[counter])


