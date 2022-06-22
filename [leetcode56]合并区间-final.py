#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Solution:
    def merge(self, intervals):
        # 首先要对区间进行排序
        if len(intervals) == 1:
            return intervals
        intervals.sort(key=lambda x: x[0]) # 这里排序是升序排序
        result = []
        result.append(intervals[0])
        for i in range(1, len(intervals)):
            last = result[-1] # 取result里最后一个元素
            if intervals[i][0] <= last[1]: # 右边界
                #result[-1] =[last[0],max(intervals[i][1],last[1])]
                # 更新最新区间的右边界
                result[-1][1] = max(intervals[i][1],last[1])
            else:
                result.append(intervals[i])
        return result
            

intervals1 = [[1,4],[4,5]]
intervals2 = [[1,3],[2,6],[8,10],[15,18]]
