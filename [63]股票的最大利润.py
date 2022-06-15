#!/usr/bin/env python3
# -*- coding: utf-8 -*-
class Solution:
    def maxProfit(self, prices):
        # 第一步，构建一个新列表，存储第i天（包含）价格的最小值
        min_list = []
        min_temp = prices[0]
        for i in prices:
            if min_temp > i:
                min_temp = i
                min_list.append(i)
            else:
                min_list.append(min_temp)
        # print(min_list) #检查中间变量
        # 第二步，再次循环，记录最大利润。
        max_profit = 0 #当交易没完成时，题目给的利润为0
        for i, value in enumerate(prices):
            if i ==0:
                continue #第一天不进行交易
            else:
                temp_profit = value - min_list[i-1] 
                if temp_profit > max_profit:
                    max_profit = temp_profit
        return max_profit
            
        
        
prices = [7,1,5,3,6,4]
print(Solution().maxProfit(prices))