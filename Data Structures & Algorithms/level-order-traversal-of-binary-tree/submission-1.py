# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict


class Solution:
    def levelOrder(self, root):
        ans = []
        def dfs(level, node):
            if not node:
                return
            if level == len(ans):
                ans.append([])
            ans[level].append(node.val)
            dfs(level + 1, node.left)
            dfs(level + 1, node.right)
        dfs(0, root)
        return ans