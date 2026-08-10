from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            if nums[0] == val:
                return 0
            else:
                return 1
        
        def swap(i: int, j: int) -> None:
            t: int = nums[j]
            nums[j] = nums[i]
            nums[i] = t

        i: int = 0
        j: int = len(nums) - 1
        while i <= j:
            if nums[i] == val:
                swap(i, j)
                j -= 1
            else:
                i += 1
        
        return i
