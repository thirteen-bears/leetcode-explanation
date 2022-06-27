#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Node(object):
    def __init__(self,value):
        self.left = None
        self.right = None
        self.value = value
        
def PreOrder(node,array =[]): # 中左右遍历
    if node == None:
        return
    array.append(node.value)
    PreOrder(node.left,array)
    PreOrder(node.right,array)
    return array
    
def InOrder(node,array =[]): # 左中右遍历
    if node == None:
        return
    InOrder(node.left,array)
    array.append(node.value)
    InOrder(node.right,array)
    return array

def PostOrder(node,array =[]): # 左右中遍历
    if node == None:
        return
    PostOrder(node.left,array)
    PostOrder(node.right,array)
    array.append(node.value)
    return array
    
#  非迭代法前序遍历
def preorderTraversal(root):
        queue = [] # 暂存待搜索的节点
        result = [] # 存储结果
        if root == None:
            return
        else:
            queue.append(root) # 加入一个元素到队列里
            while len(queue)>0:
                temp = queue.pop() # 取出队列的头元素
                result.append(temp.value) # 
                if temp.right:
                    queue.append(temp.right)
                if temp.left:
                    queue.append(temp.left)
        return result

#  非迭代法-中序遍历
# 左中右
def inorderTraversal(root):
    cur = root
    stack = []
    result = []
    if root == None: 
            return []
    while cur or stack: # 一直循环到最左的节点
        if cur: #如果当前节点不为空,则一直进入到最左的节点
            stack.append(cur)
            cur = cur.left
        else: # 跳出开始去找右节点
            cur = stack.pop()
            result.append(cur.val)
            cur = cur.right
    temp = queue.pop()
    

#  非迭代法后序遍历
def postorderTraversal(root):
        queue = [] # 暂存待搜索的节点
        result = [] # 存储结果
        if root == None:
            return []
        else:
            queue.append(root) # 加入一个元素到队列里
            while len(queue)>0:
                temp = queue.pop() # 取出队列的头元素
                result.append(temp.value) #
                if temp.left:
                    queue.append(temp.left)
                if temp.right:
                    queue.append(temp.right)
        return result[::-1]


node = Node(5)
node.left = Node(3)
node.left.right = Node(4)
node.left.left= Node(1)
node.right = Node(6)
#result = PreOrder(node)
print("inoder:",InOrder(node, array = [])) # array需要传进去空值，否则会继承之前的值
print("preoder:",PreOrder(node, array = []))
print("preoder_new:",preorderTraversal(node))
print("postoder:",PostOrder(node, array = []))
