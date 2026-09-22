from collections import defaultdict, deque


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prereq_to_nxt = defaultdict(set)
        indegree = [0] * numCourses
        # Build map prereq to next courses
        for nxt, pre in prerequisites:
            prereq_to_nxt[pre].add(nxt)
            indegree[nxt] += 1
        # Pick up ones with 0 incoming to seed BFS
        q = deque(i for i in range(numCourses) if indegree[i] == 0)
        while q:
            c = q.popleft()
            numCourses -= 1
            nxt_crses = prereq_to_nxt[c]
            for nxt_crs in nxt_crses:
                indegree[nxt_crs] -= 1
                if indegree[nxt_crs] == 0:
                    q.append(nxt_crs)
        return numCourses == 0

        # Decrement indegrees, pick up 0 as next step

        # Check all indegrees 0