class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        idx_num_sorted = [(idx, n) for idx, n in enumerate(nums)]
        idx_num_sorted.sort(key=lambda x: x[1])
        print(idx_num_sorted)
        i, j = 0, len(nums) - 1
        while i < j:
            if idx_num_sorted[i][1] + idx_num_sorted[j][1] == target:
                ans = [idx_num_sorted[i][0], idx_num_sorted[j][0]]
                ans.sort()
                return ans

            if idx_num_sorted[i][1] + idx_num_sorted[j][1] > target:
                j -= 1
            else:
                i += 1
        
        return [0, 0]