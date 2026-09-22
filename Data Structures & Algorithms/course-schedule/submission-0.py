from collections import defaultdict, deque


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Get prereq to next map
        prereq_to_next = defaultdict(set)
        course_to_indegree = [0 for _ in range(numCourses)]
        for a, b in prerequisites:
            prereq_to_next[b].add(a)
            # Track incoming edges for each course
            course_to_indegree[a] += 1
        q = deque([])
        for idx, count in enumerate(course_to_indegree):
            if count == 0:
                q.append(idx)
        # BFS: take ones with 0 incoming, decrement as you go and if 0 add to q
        while q:
            numCourses -= 1
            course = q.popleft()
            nxt = prereq_to_next[course]
            for c in nxt:
                course_to_indegree[c] -= 1
                if course_to_indegree[c] == 0:
                    q.append(c)
        return numCourses == 0
        
        # 
        