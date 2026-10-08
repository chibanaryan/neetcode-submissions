# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node: TreeNode, min_bound: float=float('-inf'), max_bound: float=float('inf')) -> bool:
            if not node:
                return True
            if not min_bound < node.val < max_bound:
                return False
            return dfs(node.left, min_bound, node.val) and dfs(node.right, node.val, max_bound)
        return dfs(root)