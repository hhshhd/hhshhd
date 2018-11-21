#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 21 08:14:30 2018

@author: hhshhd
"""

class Node:
    def __init__(self,origin_data):
        self.data = origin_data
        self.next = None
    
    def __str__(self):
        return str(self.data) 
    
    def get_data(self):
        return self.data
    
    def get_next(self):
        return self.next
    
    def set_new_data(self,new_data):
        self.data = new_data
    
    def set_next(self,new_next):
        self.next = new_next
        
class Linked_list:
    def __init__(self):
        self.head = None
        
    def __str__(self):
        return str(self.head)
    
    def isEmpty(self):
        return self.head == None
    
    def add(self,item):
        l_l = Node(item)
        l_l.set_next(self.head)
        self.head = l_l
        
    def remove(self,item):
        pre = None
        l_l = self.head
        while l_l.get_data() != item :
            pre = l_l
            l_l = l_l.get_next()
        pre.set_next(l_l.get_next())

    def search(self,item):
        pre = None
        l_l = self.head
        while l_l.get_data() != item :
            pre = l_l
            l_l = l_l.get_next()
        if l_l.get_data() == item:
            return True
        else:
            return False
    def append(self,item):
        pre = None
        l_l = self.head
        while l_l.get_next() != None :
            pre = l_l
            l_l = l_l.get_next()
        new_node = Node(item)
        l_l.set_next(new_node)
        
    def index(self,item):
        # Assuming the nearest node is the 0th.
        pre = None
        l_l = self.head
        count = 0
        while l_l.get_data() != item :
            pre = l_l
            l_l = l_l.get_next()
            count += 1
        return count
    
    def insert(self,pos,item):
        # Assuming the nearest node is the 0th
        pre = None
        l_l = self.head
        count = 0
        while count != pos:
            pre = l_l
            l_l = l_l.get_next()
            count += 1
        new_node = Node(item)
        pre.set_next(new_node)
        new_node.set_next(l_l)
    def size(self):
        l_l = self.head
        count = 0
        while l_l != None:
            count += 1
            l_l = l_l.get_next()
        return count
    

       
       
a = Linked_list()
a.add(1) 
a.add(2)
a.add(5)
a.add(6)
a.remove(5)
a.append(7)
a.insert(1,4)
print(a.size())
print(a.isEmpty())
print(a.search(6))
print(a.index(6))
print(a.search(7))
print(a.search(4))