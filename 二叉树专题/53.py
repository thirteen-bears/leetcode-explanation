#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Solution:
    def search(self, nums, target):
        left = 0
        right = len(nums)-1
        while left <= right: # 为什么这里要加等号
            mid = (left+right)//2 
            print("left:",left)
            print("right:",right)
            print("mid:",mid)
            print("---------------")
            if target < nums[mid]: # 此时target一定在mid的左边
                right = mid-1
            elif  target > nums[mid]:# 此时target一定在mid的右边
                left = mid+1
            else: 
                
        return right - left +1


nums = [5,7,7,8,8,10]
target = 8
#nums = [1,2,2]
#target = 2
print(Solution().search(nums,target))


