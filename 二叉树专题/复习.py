#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  6 12:43:36 2022

@author: huhan
"""
class Node(object):
    def __init__(self,value):
        self.left = None
        self.right = None
        self.value = value


def InOrder(node,array =[]): # array在这里初始化
    InOrder(node.left
        
def PreOrder(node,array = []):
    

def PostOrder(node,array = []):
    
        
    

node = Node(5)
node.left = Node(3)
node.left.right = Node(4)
node.left.left= Node(1)
node.right = Node(6)
#result = PreOrder(node)
print("inoder:",InOrder(node, array = [])) # 中序遍历
print("preoder:",PreOrder(node, array = []))
print("postoder:",PostOrder(node, array = []))