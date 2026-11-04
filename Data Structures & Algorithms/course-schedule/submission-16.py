from collections import defaultdict, deque


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Map prereq to nxt
        pre_to_nxt = defaultdict(list)
        indegree = [0] * numCourses
        for nxt, pre in prerequisites:
            pre_to_nxt[pre].append(nxt)
            indegree[nxt] += 1
        # Track inbound edges
        q = deque([])
        print(pre_to_nxt)
        print(indegree)
        for course_num, in_count in enumerate(indegree):
            if in_count == 0:
                q.append(course_num)
        while q:
            cur_course  = q.popleft()
            for nxt in pre_to_nxt[cur_course]:
                indegree[nxt] -= 1
                if indegree[nxt] == 0:
                    q.append(nxt)
                
        print(indegree)
        for i in indegree:
            if i != 0:
                return False
        return True
        # Start with 0 inbound, follow graph and decrement inbounds