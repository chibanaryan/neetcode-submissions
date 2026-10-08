# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def dfs(node: TreeNode, depth_so_far: int) -> int:
            if not node:
                return depth_so_far
            depth_so_far += 1
            return max(dfs(node.left, depth_so_far), dfs(node.right, depth_so_far))
        return dfs(root, 0)