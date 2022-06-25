#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 15 01:24:24 2022

@author: huhan
"""
class Tree(object):
    def __init__(self):
        Tree.root = None

class Node(object):
    def __init__(self,value):
        self.parent = None
        self.value = value
        self.left = None
        self.right = None


def TreeInsert(T,z):
    x = T.root
    if x == None:
        z.value = T.root
    else:
        if z.value < x:
            x.left = z.value
        else:
            x.right = z.value
        
    

#构造二叉树实例对象
node=[5,9,6,8,7,2,1,10]
T=Tree()

#插入二叉树数据
for nodes in node:
    print('插入数据',TreeInsert(T,Node(nodes)))