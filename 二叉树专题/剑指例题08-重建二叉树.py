#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 23 06:34:18 2022

@author: huhan
"""

class TreeNode(object):
    def __init__(self,x):
        self.left = None
        self.right = None
        self.val = x
        
class NullNode(object):
    def __init__(self):
        self.left = None
        self.right = None
        self.val = None
'''
class Solution:
    # 函数后面跟着的箭头是函数返回值的类型建议符，用来说明该函数返回的值是什么类型。
    # 函数参数中的冒号是参数的类型建议符，告诉程序员希望传入的实参的类型（这个类型也可以自己定义的类）
    # def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
    def buildTree(self, preorder,inorder)->TreeNode:
        index = {val:i for i,val in enumerate(inorder)} # 建立字典方便从中序序列里取值
        # construct 函数是在build tree的内部调用的，所以必须在其内部进行定义
        def construct(preRootId,inL,inR): # inL,inR 为中序序列中的左右边界
            if inL>inR:
                return None  # 递归中一定要有一个递归的出口
            rootVal = preorder[preRootId]
            inRootId = index[rootVal]
            leftSize = inRootId - inL
            root = TreeNode(rootVal)
            root.left = construct(preRootId+1, inL, inRootId-1)
            root.right = construct(preRootId+leftSize+1, inRootId+1, inR)
            return root
        
        return construct(0, 0, len(inorder)-1)
'''
    
class Solution:
    def buildTree(self, preorder, inorder) -> TreeNode:
        if len(preorder)==0:
            return None
        node = TreeNode(preorder[0])
        if len(preorder)==1:
            return node
        t : int = 0
        #找出 根节点在 中序遍历中的位置，来区分左右子树。而t+1则是前序遍历中区分左右子树的前序遍历的位置。
        for i in range(len(inorder)):
            if inorder[i]==preorder[0]:
                t = i
                break
        node.left = self.buildTree(preorder[1:t+1],inorder[0:t])
        node.right = self.buildTree(preorder[t+1:],inorder[t+1:])
        return node


preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
sol = Solution()

result = sol.buildTree(preorder, inorder)

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
def DFS(root):
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

# 后序遍历
def PostOrder(node,array = []):
    if node is None:
        return []
    else:
        PostOrder(node.left,array)
        PostOrder(node.right,array)
        array.append(node.val) 
    return array

print(BFS(result))
print(PostOrder(result))
