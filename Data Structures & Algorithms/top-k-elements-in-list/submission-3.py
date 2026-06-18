from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter(nums)
        cnt_num_pairs = []
        print(c.items())
        for num, cnt in c.items():
            cnt_num_pairs.append([cnt, num])
        cnt_num_pairs.sort(key=lambda x:-x[0])
        return [x[1] for x in cnt_num_pairs[:k]]