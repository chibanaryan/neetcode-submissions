from collections import deque

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        leftwise_product = []
        product_so_far = 1
        for n in nums:
            product_so_far *= n
            leftwise_product.append(product_so_far)
        rightwise_product = deque()
        product_so_far = 1
        for n in reversed(nums):
            product_so_far *= n
            rightwise_product.appendleft(product_so_far)
        ans = []
        i = 0
        print(leftwise_product)
        print(rightwise_product)
        while i < len(nums):
            product = 1
            if i > 0:
                product *= leftwise_product[i-1]
            if i < (len(nums) - 1):
                product *= rightwise_product[i+1]
            ans.append(product)
            i += 1
        return ans