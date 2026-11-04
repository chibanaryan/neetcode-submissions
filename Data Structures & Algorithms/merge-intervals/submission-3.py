class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        ans = []
        intervals.sort(key=lambda x:(x[0], x[1]))
        prev = None
        for start, end in intervals:
            if prev is None:
                prev = [start, end]
                continue
            if prev[0] <= start <= prev[1]:
                prev[1] = max(prev[1], end)
            else:
                ans.append(prev)
                prev = [start, end]
        ans.append(prev)
        return ans
