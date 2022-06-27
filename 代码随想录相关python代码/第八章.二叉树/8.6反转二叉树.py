#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 226. 翻转二叉树
# 递归法
class Solution1:
    def invertTree(self, root) :
        if not root: # 到底
            return None
        root.left, root.right = root.right, root.left #中，这样的写法避免引入中间变量temp
        self.invertTree(root.left) #左
        self.invertTree(root.right) #右
        return root
# 前序遍历法:迭代法写前序遍历的算法
class Solution2:
    def invertTree(self, root):
        if not root:
            return root
        st = []
        st.append(root)
        while st:
            node = st.pop()
            node.left, node.right = node.right, node.left #中
            if node.right:
                st.append(node.right) #右
            if node.left:
                st.append(node.left) #左
        return root
# 层序遍历法
import collections
class Solution3:
    def invertTree(self, root):
        queue = collections.deque() #使用deque()
        if root:
            queue.append(root)
        while queue:
            size = len(queue)
            for i in range(size):
                node = queue.popleft()
                node.left, node.right = node.right, node.left #节点处理
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return root