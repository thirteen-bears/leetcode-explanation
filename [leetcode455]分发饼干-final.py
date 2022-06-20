#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 贪心算法典型题
class Solution:
    def findContentChildren(self, g, s) -> int:
        count = 0
        for j in s:# 对每个饼干进行循环
            # 找到g中最小的大于等于s的数值
            temp = []
            for i in g: # 对每个饼干挑选出合适的孩子
                if i<=j: # 如果孩子的食量小于饼干
                    temp.append(i)
            if len(temp)>0: # 这么写是不对的，oooo
                g.remove(min(temp))
                count+=1
            else:
                continue
        return count

g = [10,9,8,7]
s = [10,9,8,7]
print(Solution().findContentChildren(g, s))
