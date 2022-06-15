#!/usr/bin/env python3
# -*- coding: utf-8 -*-
class Solution:
    def maxSubArray(self, nums):
        init_status = nums[0]
        pre_max = init_status 
        count = 1
        general_max = pre_max 
        while count <= len(nums)-1:
            # 这几行是动态规划更新方程
            if pre_max < 0:
                cur_max = nums[count]
            else:
                cur_max = nums[count]+ pre_max
            # 更新传递变量
            pre_max = cur_max
            # 更新计数变量
            count +=1
            # 求最大值
            if  cur_max> general_max:
                general_max = cur_max
            #print(cur_max)
        return general_max
        
        
        
        
        
        
        
        
        
        
nums = [-2,1,-3,4,-1,2,1,-5,4]
print(Solution().maxSubArray(nums))