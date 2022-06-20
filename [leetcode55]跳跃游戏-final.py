#!/usr/bin/env python3
# -*- coding: utf-8 -*-
class Solution:
    def canJump(self, nums) :
        # 这道题的难点在于想明白想通，难在对算法的理解上。
        # 用贪心算法这道题会很简单。
        # 举个极端的例子：
        # [1,0,0,0,100,0,0,0,0] index(为2)<cover(当前可覆盖距离)
        # index = 2 在index = 0,1的最远距离之外，所以压根到不了
        # 继续来看这道题的思路：
        # 对数组中任意一个元素y，判断y是否能到达
        # 只需要存在x,x+nums[x]>=y，y即可到达
        
        cover = 0
        # 先写通用情况，然后返回看特殊情况
        if len(nums) == 1:
            return True
        for i in range(len(nums)-1): #注意这里是-1，因为不考虑最后一个元素，因为最后一个元素不用继续延伸。
            # 不断更新cover和nums的值
            # 如果有cover<i,就证明当前i是到达不了的
            if cover<i:
                return False
            cover = max(i+nums[i],cover) 
            if cover>= len(nums)-1:
                return True
        return False
            

        

nums = [2,3,1,1,4] # true