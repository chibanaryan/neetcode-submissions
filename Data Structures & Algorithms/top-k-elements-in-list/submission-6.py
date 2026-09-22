from collections import defaultdict, Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_to_count = Counter(nums)
        count_to_nums = defaultdict(list)
        for num, count in num_to_count.items():
            count_to_nums[count].append(num)
        res = []
        for i in range(len(nums), 0, -1):
            if len(res) > k:
                break
            if count_to_nums[i]:
                res.extend(count_to_nums[i])
        return res[:k]