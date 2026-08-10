class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        r = [1] * n

        left_product = 1
        for i in range(n):
            r[i] = left_product
            left_product *= nums[i]

        right_product = 1
        for i in range(n - 1, -1, -1):
            r[i] *= right_product
            right_product *= nums[i]

        return r
