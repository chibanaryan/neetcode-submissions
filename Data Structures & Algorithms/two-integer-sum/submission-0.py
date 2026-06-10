class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        remaining_to_idx = {}
        for idx, num in enumerate(nums):
            remaining = target - num
            if num in remaining_to_idx:
                return [remaining_to_idx[num], idx]
            remaining_to_idx[remaining] = idx
        return None