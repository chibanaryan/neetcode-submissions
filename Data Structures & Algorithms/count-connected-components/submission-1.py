from collections import defaultdict, deque


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        connections = defaultdict(list)
        for a, b in edges:
            connections[a].append(b)
            connections[b].append(a)
        
        # Iterate from 0 to n, if new unvisited node increment and recursively mark neighbors visited
        count = 0
        visited = set()
        for i in range(n):
            if i in visited:
                continue
            count += 1
            visited.add(i)
            q = deque([i])
            while q:
                a = q.popleft()
                for b in connections[a]:
                    if b not in visited:
                        visited.add(b)
                        q.append(b)
            i += 1
        return count