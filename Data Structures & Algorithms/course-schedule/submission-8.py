from collections import defaultdict


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prereq_to_nxt = defaultdict(list)
        indegree = [0] * numCourses
        for nxt, pre in prerequisites:
            prereq_to_nxt[pre].append(nxt)
            indegree[nxt] += 1
        
        q = deque([])
        for course, cnt in enumerate(indegree):
            if cnt == 0:
                q.append(course)

        while q:
            cur = q.popleft()
            numCourses -= 1
            for nxt in prereq_to_nxt[cur]:
                indegree[nxt] -= 1
                if indegree[nxt] == 0:
                    q.append(nxt)

        return numCourses == 0



        # Indegree for course
        # Take all with 0, reduce indegree of following
