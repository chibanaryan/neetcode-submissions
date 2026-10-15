class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest = float('inf')
        best = 0
        for p in prices:
            lowest = min(lowest, p)
            best = max(p - lowest, best)
        return max(best, 0)
