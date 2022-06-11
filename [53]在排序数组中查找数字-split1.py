#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def binarySearchLeft(nums,target):
    left = 0
    right = len(nums)-1
    target_left_bound = -1
    while left <=right: 
        mid = (left+right)//2
        if nums[mid] ==target:
            target_left_bound  = mid
            right = mid-1

        elif nums[mid]< target:
            left = mid+1 
        else: 
            right = mid-1
    return target_left_bound 

def binarySearchRight(nums,target):
    left = 0
    right = len(nums)-1
    target_right_bound = -1
    while left <=right: 
        mid = (left+right)//2
        if nums[mid] ==target:
            target_right_bound  = mid
            left = mid+1 #[mid+1,right]是否含有target

        elif nums[mid]< target:
            left = mid+1 
        else: 
            right = mid-1
    return target_right_bound 


    
nums = [5,8,8,8,8]
target = 8
print(binarySearchLeft(nums, target))
print(binarySearchRight(nums, target))
