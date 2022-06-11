#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Solution:
    def missingNumber(self, nums):
        left = 0
        right = len(nums)-1
        missing_number = 0
        flag = 0 # flag为0代表数组没有任何缺失元素。
        while left <=right: 
            mid = (left+right)//2
            if nums[mid] == mid:# 说明缺失元素在[mid+1,right]之间
                left = mid+1
            else:  # nums[mid]>mid #说明mid可能是缺失元素，也可能缺失元素在[left,mid-1]之间
                missing_number = mid
                right = mid-1
                flag = 1
        if flag == 0:
            missing_number = nums[-1]+1
        return missing_number
    
nums = [0,1,2,3] # 4
print(Solution().missingNumber(nums))
        