# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(node: TreeNode, min_bound=None, max_bound=None) -> bool:
            if not node:
                return True
            if (min_bound is not None and min_bound >= node.val) or (max_bound is not None and max_bound <= node.val):
                return False
            return dfs(node.left, min_bound, node.val) and dfs(node.right, node.val, max_bound)
        
        return dfs(root)