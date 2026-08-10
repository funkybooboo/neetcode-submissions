from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if not nums or len(nums) == 1:
            return

        def swap(i: int, j: int) -> None:
            t: int = nums[i]
            nums[i] = nums[j]
            nums[j] = t

        e: int = len(nums)
        p: int = 0
        while p < e:
            if nums[p] == 0:
                s: int = p
                while s + 1 < e:
                    swap(s, s + 1)
                    s += 1
                e -= 1
            else:
                p += 1
