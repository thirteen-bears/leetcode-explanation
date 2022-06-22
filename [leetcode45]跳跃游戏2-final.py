#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# 错误例子
# 
'''
class Solution:
    def jump(self, nums):
        cover  = 0
        if len(nums) ==1:
            return 0
        for i in range(len(nums)-1):
            cover = max(cover, nums[i]+i)
            if cover>=len(nums)-1:
                return i+1
            '''
# 反例:[2,3,1,1,4]
# 反例：[1,2,1,1,1] 
# 难点：怎么计算真正的步数？
# 第一次到达max时候的i1,第一次到达i1时候的i2，逆向推导到index= 0
class Solution:
    def jump(self, nums):
        if len(nums) == 1: return 0
        ans = 0 # 记录当前步数
        curDistance = 0 # 记录当前最远距离
        nextDistance = 0 # 记录下一步的最远距离
        for i in range(len(nums)):
            nextDistance = max(i + nums[i], nextDistance) # 统计下一步的最大覆盖范围，i == curDistance的情况也要算上
            if i == curDistance:
                if curDistance != len(nums) - 1: # 当前没有达到终点,这里的”不等于“一定是”小于等于“
                    ans += 1 # 则需要继续走，步数增加1
                    curDistance = nextDistance # 下一步的最大达到范围复制给当前最大到达                    if nextDistance >= len(nums) - 1:  # 如果下一步到达范围超过了终点，则返回当前步数（已经+1）
                        break
        return ans
            