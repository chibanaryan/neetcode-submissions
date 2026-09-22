"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from collections import deque


class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
            
        org_to_new = {}
        org_to_new[node] = Node(node.val)
        q = deque([node])
        while q:
            cur = q.popleft()
            for nei in cur.neighbors:
                if nei not in org_to_new:
                    org_to_new[nei] = Node(nei.val)
                    q.append(nei)
                org_to_new[cur].neighbors.append(org_to_new[nei])
        return org_to_new[node]