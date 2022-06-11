#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Solution:
    def search(self, nums, target):
        def binarySearch(nums,target,isLeftBound):
            left = 0
            right = len(nums)-1
            target_bound = -1
            while left <=right: 
                mid = (left+right)//2
                if nums[mid] ==target:
                    target_bound  = mid
                    if isLeftBound:
                        right = mid-1
                    else:
                        left = mid+1
                elif nums[mid]< target:
                    left = mid+1 
                else: 
                    right = mid-1
            return target_bound 
        
        left_bound = binarySearch(nums,target,True)
        if left_bound == -1:
            return 0
        else:
            right_bound = binarySearch(nums,target,False)
        return right_bound -left_bound+1


nums = [5,8,8,8,8]
target = 8
print(Solution().search(nums, target))