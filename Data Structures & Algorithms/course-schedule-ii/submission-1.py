from collections import defaultdict, deque


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        res = []
        pre_to_nxt = defaultdict(list)
        indegree = [0] * numCourses
        for nxt, pre in prerequisites:
            pre_to_nxt[pre].append(nxt)
            indegree[nxt] += 1
        q = deque([])
        visited = set()
        for course_num, count in enumerate(indegree):
            if count == 0:
                res.append(course_num)
                visited.add(course_num)
                q.append(course_num)
        while q:
            c_crs = q.popleft()
            for nxt in pre_to_nxt[c_crs]:
                indegree[nxt] -= 1
                if indegree[nxt] == 0 and nxt not in visited:
                    q.append(nxt)
                    res.append(nxt)
        if len(res) < numCourses:
            return []
        return res


        