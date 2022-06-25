#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 23 22:39:06 2022

@author: huhan
"""
# 层次遍历（广度优先）
def BFS(root):
    if root:
        res = []
        queue = [root]
        while queue:
            currentNode = queue.pop(0)
            res.append(currentNode.val)
            if currentNode.left:
                queue.append(currentNode.left)
            if currentNode.right:
                queue.append(currentNode.right)
    return res






# 深度优先
'''
深度优先搜索的步骤分为 1.递归下去 2.回溯上来。
顾名思义，深度优先，则是以深度为准则，先一条路走到底，直到达到目标。这里称之为递归下去。
否则既没有达到目标又无路可走了，那么则退回到上一步的状态，走其他路。这便是回溯上来。
'''
def DFS(root):
    if root:
        res = []
        stack = [root]
        while stack:
            # pop() 函数用于移除列表中的一个元素（默认最后一个元素），并且返回该元素的值。
            currentNode = stack.pop() 
            res.append(currentNode.val)
            # 放进去的时候先右后左，这样从后面取出来的时候就是先左后右了
            if currentNode.right:
                stack.append(currentNode.right)
            if currentNode.left:
                stack.append(currentNode.left)
    return res

