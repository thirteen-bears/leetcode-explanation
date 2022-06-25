#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 2022.01.14
# n为树的节点个数
# 时间复杂度 O(n) 遍历二叉搜索树的每一个节点
# 空间复杂度 O(n) 遍历到的节点存到一个列表里

class BST: 
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

def inOrderArray(tree, array = []):
    if tree is None:
        return []
    else:
        inOrderArray(tree.left,array)
        array.append(tree.value)
        inOrderArray(tree.right,array)
    return array


def postOrderArray(tree, array = []):
    if tree is None:
        return []
    else:
        postOrderArray(tree.left,array)
        postOrderArray(tree.right,array)
        array.append(tree.value)
    return array

def preOrderArray(tree, array = []):
    if tree is None:
        return []
    else:
        array.append(tree.value)
        preOrderArray(tree.left,array)
        preOrderArray(tree.right,array)
    return array

root = BST(10)
root.left = BST(5)
root.right = BST(15)
root.left.left = BST(2)
root.left.right = BST(5)
root.right.right = BST(22)
root.left.left.left = BST(1)

print('inOrderArray:',inOrderArray(root, array = []))
print('postOrderArray:',postOrderArray(root, array = []))
print('preOrderArray:',preOrderArray(root, array = []))