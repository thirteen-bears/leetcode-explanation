#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Solution:
    def lengthOfLongestSubstring(self, s):
        # 还是从末尾找状态转移方程
        # 以n结尾的最长字符串

        # dp[n] = dp[n-1] +1  如果第n个数字不跟前面的重复
        # 或者  dp[n] = dp[n-1] 如果第n个数字跟前面的重复了
        # 这道题类似于前面的一道连续最大之和的题目
        # 关于连续的题目，都请转化成
        list_max = []
        init_0 = 1
        pre_status = init_0
        if len(s) == 0:
            list_max.append(0)
        for i in range(len(s)):
            # 初始状态
            if i == 0:
                list_max.append(init_0)
            else:
                if s[i] in s[0:i]:
                    cur_status = 1 
                else:
                    cur_status = pre_status+1
                pre_status = cur_status
                list_max.append(cur_status)
                print(list_max) #print中间过程
        return max(list_max)
                

#s = "abcabcbb"
# s = "bbbbbb"
s = "pwwkew"
print(Solution().lengthOfLongestSubstring(s))