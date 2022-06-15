#!/usr/bin/env python3
# -*- coding: utf-8 -*-
class Solution:
    def translateNum(self, num):# num是int格式
        # 状态转移方程： 
        # 
        # 最后一个种类n = (n-2)种类+(n-1)的种类 if n-2~n在0~25之间
        # 最后一个种类n = (n-1)的种类 if n-2~n>25
        # 因为这里是n-2 所以要求出前两个初始状态
        str_num = str(num)
        init_0 = 1
        if len(str_num) == 1:
            return init_0 
        if int(str_num[0:2])<=25:
            init_1 = 2 # 两种翻译方法
        else:
            init_1 = 1 # 一种翻译方法
        
        if len(str_num) == 1:
            return init_1
        
        count = 2
        while count <= len(str_num)-1:
            if int(str_num[count+1-2:count+1])<=25:
                init_cur = init_0+init_1
            else:
                init_cur = init_1
            temp = init_1
            init_1 = init_cur
            init_0 = temp
            count+=1
        return init_cur 


num = 12258
print(Solution().translateNum(num))
