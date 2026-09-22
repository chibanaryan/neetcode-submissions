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
        i = 0
        while i < n:
            if i not in visited:
                count += 1
                q = deque([i])
                while q:
                    a = q.popleft()
                    for b in connections[a]:
                        if b not in visited:
                            visited.add(b)
                            q.append(b)
            i += 1
        return count

                
        
        # q = deque([i for i, c in enumerate(indegree) if c == 0])
        # while q:
        #     a = q.popleft()
        #     for b in connections[a]:
        #         indegree[b] -= 1
        #         if indegree[b] == 0:
        #             q.append(b)
