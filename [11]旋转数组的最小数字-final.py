#!/usr/bin/env python3
# -*- coding: utf-8 -*-
class Solution:
    def minArray(self, numbers: List[int]) -> int:
        # 原来是升序排列，只进行了一次旋转
        # 那么存在分段的升序关系
        # 还是用二分法
        # 如果有升序关系，最小值不存在于这个区间
        