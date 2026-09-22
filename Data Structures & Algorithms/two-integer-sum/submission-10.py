class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        remainder_to_idx = {}
        for i, n in enumerate(nums):
            if n in remainder_to_idx:
                return [remainder_to_idx[n], i]
            remainder_to_idx[target - n] = i
        return ValueError("no solution")
        