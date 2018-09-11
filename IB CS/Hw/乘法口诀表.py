#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 11 15:49:42 2018

@author: hhshhd
"""
start=int(input('number:'))
x=0
y=0
while x!=start:
    print('\n')
    x+=1
    y=0
    for i in range(x):
        y+=1
        print(x,'*',y,'=',x*y,'', end='')
else:
    print('')
