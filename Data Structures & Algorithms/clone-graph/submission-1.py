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
        node_map = {}
        if not node:
            return None

        q = deque([node])
        visited = set()
        visited.add(node)
        while q:
            print(q)
            cur = q.popleft()

            if cur not in node_map:
                new_node = Node(cur.val)
            else:
                new_node = node_map[cur]

            for n in cur.neighbors:
                if n not in node_map:
                    new_n = Node(n.val)
                    node_map[n] = new_n
                new_node.neighbors.append(node_map[n])
                if n not in visited:
                    visited.add(n)
                    q.append(n)        
                    
            node_map[cur] = new_node            

        return node_map[node]


                    
                    