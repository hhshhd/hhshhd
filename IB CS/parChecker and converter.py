#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 14 09:09:47 2018

@author: hhshhd
"""

class Stack:
     def __init__(self):
         self.stack = []

     def isEmpty(self):
         return self.stack == []

     def push(self, item):
         self.stack.append(item)

     def pop(self):
         return self.stack.pop()

     def peek(self):
         return self.stack[-1]

     def size(self):
         return len(self.stack)

def parChecker(String):
    kuohao = Stack()
    position = 0
    while position < len(String):
        item = String[position]
        if item in "([{":
            kuohao.push(item)
        else:
            if kuohao.isEmpty():
                return False
            else:
                top = kuohao.pop()
                if (top == '(' and item == ')') or (top == '[' and item == ']') or (top == '{' and item == '}'):
                    None
                else:
                    return False
        position = position + 1
    if kuohao.isEmpty():
        return True
    else:
        return False

#def matches(open,close):
#    opens = "([{"
#    closers = ")]}"
#    return opens.index(open) == closers.index(close)

def decibina(num):
    temp = Stack()
    while num > 0:
        item = num % 2
        temp.push(item)
        num = num // 2
    result = ''
    while temp.size()>0:
        result = result + str(temp.pop())
    return result

def deci_n(num,n):
    Range = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    temp = Stack()

    while num > 0:
        item = num % n
        temp.push(item)
        num = num // n
    result = ''
    while temp.size()>0:
        result = result + Range[temp.pop()]

    return result

print(parChecker('[]{{}'))
print(parChecker('(([]{}{}))'))
print(decibina(25))
print(deci_n(50,11))

