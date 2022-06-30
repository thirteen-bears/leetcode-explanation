#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        # 中序：左中右； 后序：左右中
        # 第一步：先进行初始化，找后序的第一个节点
        if not postorder:
            return None

        # 第二步：建立第一个根节点
        root_val = postorder[-1]
        root = TreeNode(root_val)

        # 第三步：在中序中定位后序节点，即切割点。注意python中定位为index
        separator_idx  = inorder.index(root_val) # 返回定位的位置坐标

        # 第四步：分割中序数组：
        # python的语法是左闭右开，所以我们先要弄清具体包含哪些元素再去写边界
        inorder_left = inorder[0:separator_idx]
        inorder_right = inorder[separator_idx+1:] # 必须包含最后一个元素
        
        # 第五步：分割后序数组：长度与中序数组一致
        #postorder.pop(-1) # 剔除后序数组最后一个元素
        postorder_left = postorder[0:len(inorder_left)]
        # 这里用了-1，即不包含最后一个元素，所以可以省略pop那句了。
        postorder_right = postorder[len(inorder_left):-1]
        # 第六步：进行递归，注意调用函数本身的时候要加self
        root.left = self.buildTree(inorder_left,postorder_left)
        root.right = self.buildTree(inorder_right,postorder_right)
        return root