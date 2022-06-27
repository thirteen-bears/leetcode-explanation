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
        def backtracking(n,k,sum,startIndex):
            if sum >n:
                return
            if len(path) == k:
                if sum == n:
                    result.append(path[:])
                return
            for i in range(startIndex,10): # 显然startIndex从1开始，为了能取到1，终止于10
                path.append(i)
                sum+=i
                backtracking(n, k,sum, i+1)
                sum -=i
                path.pop()
        backtracking(n,k,0,1)
        return result
                           
n = 9 # 和为n
k = 3 # k个数
result = Solution().combine(n, k)
print(result)
