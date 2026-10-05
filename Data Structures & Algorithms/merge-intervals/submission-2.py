class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        prev = None
        intervals.sort(key=lambda x:(x[0], x[1]))
        for i in intervals:
            if not prev:
                prev = i
                continue
            if prev[1] >= i[0]:
                prev[1] = max(prev[1], i[1])
            else:
                res.append(prev)
                prev = i
        res.append(prev)
        return res