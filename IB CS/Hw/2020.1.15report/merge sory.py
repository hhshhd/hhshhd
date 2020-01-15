#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 15 09:06:51 2020

@author: hhshhd
"""

dlist = input('input list:')

def merge_sort_part2(lef,righ):
    result = []
    temp = Temp = 0
    while Temp < len(lef) and temp < len(righ):
        if lef[Temp] < righ[temp]:
            result.append(lef[Temp])
            Temp += 1
        else:
            result.append(righ[temp])
            temp += 1

    if Temp == len(lef):
        for i in righ[temp:]:
            result.append(i)
    else:
        for i in lef[Temp:]:
            result.append(i)

    return result
        
    
def merge_sort_part1(dlist):
    n = len(dlist)
    if n <= 1:
        return dlist
    mid = n//2
    left = merge_sort_part1(dlist[:mid])
    right = merge_sort_part1(dlist[mid:])
    return merge_sort_part2(left,right)

