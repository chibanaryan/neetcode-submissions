# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def dfs(node: TreeNode, max_above: float=float('-inf')):
            if not node:
                return 0
            if node.val < max_above:
                max_above = max(max_above, node.val)
                return 0 + dfs(node.left, max_above) + dfs(node.right, max_above)
            max_above = max(max_above, node.val)
            return 1 + dfs(node.left, max_above) + dfs(node.right, max_above)

        return dfs(root)