import heapq
from collections import defaultdict


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ctr = Counter(nums)
        h = []
        for num, count in ctr.items():
            heapq.heappush(h, (count, num))
            if len (h) > k:
                heapq.heappop(h)
        return [n[1] for n in h]