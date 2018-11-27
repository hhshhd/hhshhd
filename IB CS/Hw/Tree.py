#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 27 15:34:55 2018

@author: hhshhd
"""

class Tree:
    def __init__(self,cargo,left = None,right = None):
        self.cargo = cargo
        self.left = left
        self.right = right
        
    def __str__(self):
        return str(self.cargo)
    
def print_tree_preorder(tree):
    if tree is None: 
        return
    print(tree.cargo, end=" ")
    print_tree_preorder(tree.left)
    print_tree_preorder(tree.right)

def print_tree_postorder(tree):
    if tree is None: 
        return
    print_tree_postorder(tree.left)
    print_tree_postorder(tree.right)
    print(tree.cargo, end=" ")

def print_tree_inorder(tree):
    if tree is None: 
        return
    print_tree_inorder(tree.left)
    print(tree.cargo, end=" ")
    print_tree_inorder(tree.right)
    
    
t1 = Tree('a',Tree('b',Tree('d'),Tree('e')),Tree('c',Tree('f'),Tree('g')))


print(print_tree_preorder(t1))
print(print_tree_postorder(t1))
print(print_tree_inorder(t1))