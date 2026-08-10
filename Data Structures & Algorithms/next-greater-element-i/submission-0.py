from typing import List

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans: List[int] = []
        
        def find_next_biggest(j: int) -> int:
            for k in range(j + 1, len(nums2)):
                if nums2[j] < nums2[k]:
                    return nums2[k]
            return -1

        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if nums1[i] == nums2[j]:
                    ans.append(find_next_biggest(j))

        return ans
