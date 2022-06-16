#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

# 方法一：遍历法
# 删除值为 val 的节点分需为两步：定位节点、修改引用。
class Solution1:
    def deleteNode(self, head: ListNode, val: int) -> ListNode:
        if head.val == val: # 这里讨论特殊情况，删除首位
            #if head.next:
                return head.next
            #else:
                #return [] # 测试用例里不会返回空，所以这里可以不要
        cur = head # head用一个变量来替代，然后更新这个变量cur
        while cur.next:
            if cur.next.val == val:
                cur.next  = cur.next.next # cur.next存在,那么cur.next.next最坏的情况也是空，不会不存在
                break
            else:
                cur = cur.next
        return head

# 更加清晰的写法：
# 每个节点都设置一个前驱节点和一个后节点
class Solution1_1:
    def deleteNode(self, head: ListNode, val: int) -> ListNode:
        if head.val == val: # 这里讨论特殊情况，删除首位
            #if head.next:
                return head.next
            #else:
                #return [] # 测试用例里不会返回空，所以这里可以不要
        pre = head # head用一个变量来替代，然后更新这个变量cur
        cur = pre.next
        while cur:
            if cur.val == val:
                pre.next  = cur.next 
                break
            else:
                pre = cur # pre和cur都要更新不能少
                cur = cur.next
        return head

# 方法二：双指针法：即设置一个前驱节点
class Solution2:
    def deleteNode(self, head: ListNode, val: int) -> ListNode:
        if head.val == val: # 这里讨论特殊情况，删除首位
            return head.next
        pre = head # 指针1
        cur = pre.next # 指针2
        while cur:
            if cur.val == val:
                pre.next  = cur.next 
                break
            else:
                pre = cur # pre和cur都要更新不能少
                cur = cur.next
        return head

if __name__ == "__main__":
    vals = [4,5,1,9]
    
    head = ListNode(vals[0])
    cur = head
    cur.next = ListNode(vals[1])
    cur = cur.next
    cur.next = ListNode(vals[2])
    cur = cur.next
    cur.next = ListNode(vals[3])
    
    
    val = 1
    new_head = Solution1_1().deleteNode(head, val)
    
    # 打印链表
    cur = new_head
    print(cur.val)
    while cur.next:
        cur = cur.next
        print(cur.val)
        
        

