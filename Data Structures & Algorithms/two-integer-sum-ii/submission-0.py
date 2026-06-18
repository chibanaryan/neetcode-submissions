class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        remainder_to_idx = {}
        for idx, num in enumerate(numbers):
            remainder = target - num
            if num in remainder_to_idx:
                return [remainder_to_idx[num] + 1, idx + 1]
            remainder_to_idx[remainder] = idx
        return []