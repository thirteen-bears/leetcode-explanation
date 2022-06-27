#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Solution:
    def combine(self, n, k): # -> List[List[int]]
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        # 定义了两个全局变量
        result = []
        path = []
        def backtracking(n,k,startIdx):
            if len(path) == k:
                result.append(path[:])
                return
            for i in range(startIdx,n):
                path.append(i)
                backtracking(n, k, i+1)
                path.pop()
        backtracking(n,k,1)
        return result

n = 4
k = 2
result = Solution().combine(n, k)
print(result)