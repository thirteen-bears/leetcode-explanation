#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Node(object):
    def __init__(self,value):
        self.left = None
        self.right = None
        self.val = value
# ----------------------前序遍历----------------------------
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def preorder(cur, result=[]): 
            if not cur: # root为空
                return []
            result.append(cur.val)
            preorder(cur.left, result)
            preorder(cur.right, result)
            return result
        result = preorder(root)
        return result

class Solution:
    def preorderTraversal(self, root):
        # 非迭代法
        stack = []
        result = []
        if not root:
            return stack
        stack.append(root)
        while stack:
            cur = stack.pop()
            result.append(cur.val)
            if cur.right:
                stack.append(cur.right)
            if cur.left:
                stack.append(cur.left)
        return result

# ----------------------中序遍历----------------------------
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def  inorder(cur,result = []):
            if not cur:
                #return result
                return [] # 这里写return result也行
            inorder(cur.left)
            result.append(cur.val)
            inorder(cur.right)
            return result
        result = inorder(root)
        return result
  
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # 中序遍历，遍历和读取的节点不同步
        stack = []
        result = []
        if not root:
            return []
        # 先走到最左边
        cur  = root
        while cur or stack:
            if cur:
                stack.append(cur)
                cur = cur.left
        #while stack: # 其实每一个stack都要做这一步 所以合并到一起
            else:
                cur = stack.pop()
                result.append(cur.val)
                cur = cur.right
        return result
# ----------------------后序遍历----------------------------
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def postorder(root,result = []):
            if not root:
                return []
            postorder(root.left)
            postorder(root.right)
            result.append(root.val)
            return result
        result  = postorder(root)
        return result

#  非迭代法后序遍历
def postorderTraversal(root):
        queue = [] # 暂存待搜索的节点
        result = [] # 存储结果
        if root == None:
            return []
        else:
            queue.append(root) # 加入一个元素到队列里
            while len(queue)>0:
                temp = queue.pop() # 取出队列的头元素
                result.append(temp.value) #
                if temp.left:
                    queue.append(temp.left)
                if temp.right:
                    queue.append(temp.right)
        return result[::-1]


node = Node(5)
node.left = Node(3)
node.left.right = Node(4)
node.left.left= Node(1)
node.right = Node(6)
#result = PreOrder(node)
print("inoder:",InOrder(node, array = [])) # array需要传进去空值，否则会继承之前的值
print("preoder:",PreOrder(node, array = []))
print("preoder_new:",preorderTraversal(node))
print("postoder:",PostOrder(node, array = []))
