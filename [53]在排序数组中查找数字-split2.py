#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def binarySearch(nums,target,isLeft):
    left = 0
    right = len(nums)-1
    target_bound = -1
    while left <=right: 
        mid = (left+right)//2
        if nums[mid] ==target:
            target_bound  = mid
            if isLeft:
                right = mid-1
            else:
                left = mid+1
        elif nums[mid]< target:
            left = mid+1 
        else: 
            right = mid-1
    return target_bound 




nums = [5,8,8,8,8]
target = 8
print(binarySearch(nums, target,True))


