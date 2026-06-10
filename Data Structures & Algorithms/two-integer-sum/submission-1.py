class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # map of key remaining, value index
        remaining_to_idx = {}
        for idx, num in enumerate(nums):
            if num in remaining_to_idx:
                return [remaining_to_idx[num], idx]
            remaining = target - num
            remaining_to_idx[remaining] = idx
        return None