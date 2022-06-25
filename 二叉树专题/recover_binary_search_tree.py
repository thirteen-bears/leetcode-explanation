# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# link: https://www.bilibili.com/video/BV14v411n7DF?p=90
# link: https://leetcode.com/problems/recover-binary-search-tree/

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution(object):
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        self.temp = []
        def dfs(node):
            if not node:
                return
            dfs(node.left)
            self.temp.append(node)
            dfs(node.right)
        dfs(root)
        
        srt = sorted(n.val for n in self.temp) # values are in order
        
        for i in range(len(srt)):
            self.temp[i].val = srt[i]

sol = Solution()
root = [1,3,None,None,2]
answer = sol.recoverTree(root)