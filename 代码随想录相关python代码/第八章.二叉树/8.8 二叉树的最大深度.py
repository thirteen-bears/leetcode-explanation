#!/usr/bin/env python3
# -*- coding: utf-8 -*-
class Solution:
    def levelOrder(self, root):
        results = []
        if not root:
            return []

        from collections import deque # 引入队列
        que = deque([root])  # 建立队列
        # 队列里提出元素:que.popleft()
        # 队列里存入元素:que.append(node)
        count = 0
        while que:
            size = len(que) #这里的size是特定某一层的size
            result = []
            count+=1
            for _ in range(size): # 对某一层的所有节点进行遍历
                cur = que.popleft()
                result.append(cur.val)
                if cur.left:
                    que.append(cur.left)
                if cur.right:
                    que.append(cur.right)
            results.append(result)  # 把一层遍历的结果放入最后结果中
        return count