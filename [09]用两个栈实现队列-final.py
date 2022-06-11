#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class CQueue:
    def __init__(self):
        self.A = [] 
        self.B = [] 

    def appendTail(self, value: int):
        self.A.append(value)

    def deleteHead(self):
        if self.B:
            return self.B.pop()
        elif self.A:
            while self.A:
                self.B.append(self.A.pop())
            return self.B.pop()
        else:
            return -1
            
            
q = CQueue()
print(q.deleteHead())
q.appendTail(1)
q.appendTail(1)
q.appendTail(2)
print(q.deleteHead())

q.appendTail(3)
q.appendTail(4)
print(q.deleteHead())
print(q.deleteHead())
print(q.deleteHead())
print(q.deleteHead())

