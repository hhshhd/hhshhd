#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 11 23:19:24 2018

@author: hhshhd
"""

class Stack():
    def __init__(self,stack=[1,2,4,3,7,5,6]):
        self.stack = stack
    def isEmpty(self):
        return not self.stack
    def push(self,temp):
        self.stack.append(temp)
    def peek(self):
        return self.stack[-1]
    def size(self):
        return len(self.stack)
    def pop(self):
        return self.stack.pop()
    
class Queue():
    def __init__(self,Queue=[1,2,4,3,7,5,6]):
        self.Queue = Queue
    def isEmpty(self):
        return not self.Queue
    def enQueue(self,temp):
        self.Queue.insert(0,temp)
    def deQueue(self):
        return self.Queue.pop()
    def size(self):
        return len(self.Queue)
    def addRear(self,temp):
        self.Queue.insert(0,temp)
    def addFront(self,temp):
        self.Queue.append(temp)
    def removeRear(self):
        return self.Queue.pop(0)
    def removeFront(self):
        return self.Queue.pop()