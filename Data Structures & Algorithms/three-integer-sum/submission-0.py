class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        i = 0
        triplets = set()
        while i < len(nums) - 2:
            j = i + 1
            k = len(nums) - 1
            while j < k:
                summed = nums[i] + nums[j] + nums[k]
                if summed == 0:
                    triplets.add((nums[i], nums[j], nums[k]))
                    j += 1
                elif summed < 0:
                    j += 1
                else:
                    k -= 1
            i += 1
        return list(triplets)