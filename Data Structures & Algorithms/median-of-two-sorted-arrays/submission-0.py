from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2

        if len(B) < len(A):
            A, B = B, A # ensure A is smaller

        lenA = len(A)
        lenB = len(B)

        total = lenA + lenB
        half = total // 2
        left, right = 0, lenA - 1
        while True:
            midA = (left + right) // 2
            midB = (half - midA) - 2

            leftA = A[midA] if midA >= 0 else float("-inf")
            rightA = A[midA + 1] if midA + 1 < lenA else float("inf")

            leftB = B[midB] if midB >= 0 else float("-inf")
            rightB = B[midB + 1] if midB + 1 < lenB else float("inf")

            if leftA <= rightB and leftB <= rightA:
                if total % 2 == 0:
                    return (max(leftA, leftB) + min(rightA, rightB)) / 2
                else:
                    return min(rightA, rightB)
            elif leftA > rightB and leftB < rightA:
                # right partition is wrong
                right = midA - 1
            elif leftA < rightB and leftB > rightA:
                # left partition is wrong
                left = midA + 1
