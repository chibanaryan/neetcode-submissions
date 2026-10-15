class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        remainder_to_idx = {}
        for idx, num in enumerate(nums):
            remainder = target - num
            if num in remainder_to_idx:
                return [remainder_to_idx[num], idx]
            remainder_to_idx[remainder] = idx
        return None
