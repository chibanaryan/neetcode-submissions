# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, max_above):
            if not node:
                return 0
            count = 1 if node.val >= max_above else 0
            new_max = max(max_above, node.val)
            return count + dfs(node.left, new_max) + dfs(node.right, new_max)
        return dfs(root, float('-inf'))