#!/usr/bin/env python3
# -*- coding: utf-8 -*-
class Solution:
    def lemonadeChange(self, bills):
        # 不要吝啬多创建几个变量
        # 钱是无序的，不需要用队列去把钱全部存在一起
        five = 0
        ten = 0
        twenty = 0
        for i in bills:
            if i == 5: # 收入为5块
                five+=1
            elif i == 10: # 收入为10块
                if five>0:
                    five -=1
                    ten+=1
                else:# 没有零钱给10块找零
                    return False
            else: # 收入为20块
                if five > 0 and ten > 0: # 先写能找零的情况，因为情况数比不能找零的好写
                    five -= 1
                    ten -=1
                    twenty+=1 # 这一行可以删掉
                elif five>=3:
                    five -=3
                    twenty +=1#这一行可以删掉
                else:
                    return False
        return True

# 
bills = [5,5,5,20,5,5,5,20,5,5,5,10,5,20,10,20,10,20,5,5] # true
#[5,5,5,10,20]
#bills = [5,5,5,10,20]
#bills = [5,5,5,5,10,5,10,10,10,20]
bills = [5,5,10,10,20] # false
#bills = [5,5,10]
print(Solution().lemonadeChange(bills)) 