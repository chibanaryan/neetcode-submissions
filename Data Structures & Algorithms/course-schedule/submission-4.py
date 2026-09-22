from collections import defaultdict, deque


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        pre_to_nxt = defaultdict(list)
        indegree = [0 for _ in range(numCourses)]
        for nxt, pre in prerequisites:
            pre_to_nxt[pre].append(nxt)
            indegree[nxt] += 1
        q = deque([i for i, c in enumerate(indegree) if c == 0])
        taken = 0

        while q:
            taken += 1
            cur = q.popleft()
            for nxt_crs in pre_to_nxt[cur]:
                indegree[nxt_crs] -= 1
                if indegree[nxt_crs] == 0:
                    q.append(nxt_crs)
        
        return numCourses == taken
