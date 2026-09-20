class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: (x[0], x[1]))
        ans = []
        current_interval = None
        for i in intervals:
            if not current_interval:
                current_interval = i
            else:
                cl, cr = i
                if cl <= current_interval[1]:
                    current_interval[1] = max(cr, current_interval[1])
                else:
                    ans.append(current_interval)
                    current_interval = i
        ans.append(current_interval)
        return ans
