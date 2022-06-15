#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Solution:
    def maxValue(self, grid):
        if grid: # 如果grid非空
            #m = len(grid)
            #n = len(grid[0])
            # 原地修改使用常数大小的额外空间。
            # 为什么原地修改？因为之前的数字我们不再使用数字本身了
            # 如何遍历二维数组：两个for循环
            for i  in range(len(grid)):
                for j in range(len(grid[0])):
                    if i == 0 and j == 0:
                        continue
                    elif i  == 0:
                        grid[i][j] = grid[i][j-1]+grid[i][j]
                    elif j == 0:
                        grid[i][j] = grid[i-1][j]+grid[i][j]
                    else:
                        grid[i][j] = max(grid[i-1][j],grid[i][j-1])+grid[i][j]
            #return grid[m-1][n-1] #实际不用这么写的
            return grid[-1][-1]
        

grid = [
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
print(Solution().maxValue(grid))