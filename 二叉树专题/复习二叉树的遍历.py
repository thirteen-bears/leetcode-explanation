#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  6 12:55:42 2022

@author: huhan
"""
class Node(object):
    def __init__(self,value):
        self.left = None
        self.right = None
        self.val = value

def PreOrder(node,array = []):
    if node is None:
        return
    array.append(node.val)
    PreOrder(node.left,array)
    PreOrder(node.right,array)
    return array
    
def InOrder(node,array = []):
    if node is None:
        return
    InOrder(node.left,array)
    array.append(node.val)
    InOrder(node.right,array)
    return array

def PostOrder(node,array = []):
    if node is None:
        return
    PostOrder(node.left,array)
    PostOrder(node.right,array)
    array.append(node.val)
    return array

# 中序遍历的逆序遍历
def iPostOrder(node,array = []):
    if node is None:
        return
    iPostOrder(node.right,array)
    array.append(node.val)
    iPostOrder(node.left,array)
    return

node = Node(5)
node.left = Node(3)
node.left.right = Node(4)
node.left.left= Node(1)
node.right = Node(6)

print("preoder:",PreOrder(node, array = []))
print("inoder:",InOrder(node, array = []))
print("postoder:",PostOrder(node, array = []))
print("preoder:",iPostOrder(node, 1))