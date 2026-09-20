# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        level_to_vals = defaultdict(list)

        def dfs(level: int, node: TreeNode):
            if node:
                level_to_vals[level].append(node.val)
                dfs(level+1, node.left)
                dfs(level+1, node.right)

        dfs(0, root)

        ans = []
        for level in range(len(level_to_vals)):
            ans.append(level_to_vals[level])
        return ans