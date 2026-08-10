from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if n == 0:
            return

        def swap(nums: List[int], i: int, j: int) -> None:
            if not nums or i >= len(nums) or j >= len(nums):
                return
            t = nums[i]
            nums[i] = nums[j]
            nums[j] = t

        def find_leftist_zero_index(nums: List[int], m_val: int) -> int:
            for i in range(len(nums)):
                if i >= m_val:
                    return i
            return -1

        def shift_up_by_one(nums: List[int], i: int, m_val: int) -> None:
            p: int = find_leftist_zero_index(nums, m_val)
            while p - 1 >= i:
                swap(nums, p - 1, p)
                p -= 1

        i: int = 0
        j: int = 0
        while i < len(nums1) and j < len(nums2):
            if i >= m:
                nums1[i] = nums2[j]
                i += 1
                j += 1
            elif nums1[i] >= nums2[j]:
                shift_up_by_one(nums1, i, m)
                nums1[i] = nums2[j]
                j += 1
                m += 1
            else: # nums1[i] < nums2[j]
                i += 1
