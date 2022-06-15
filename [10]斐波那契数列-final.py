#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Solution:
    def fib(self, n):
        f0 = 0
        f1 = 1
        if n == 0:
            return f0
        elif n == 1:
            return f1
        else:
            count = 2
            while count <=n:
                result = f0+f1
                temp = f1
                f1 = result
                f0 = temp
                count+=1
            return result
        
print(Solution().fib(5))               
            
            