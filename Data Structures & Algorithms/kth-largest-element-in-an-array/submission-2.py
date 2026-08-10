from typing import List

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # We want the (len - k)th smallest element for kth largest
        k = len(nums) - k

        def swap(i: int, j: int):
            nums[i], nums[j] = nums[j], nums[i]

        def quick_select(l: int, r: int) -> int:
            pivot = nums[r]
            p = l

            # Partition: elements <= pivot on left, > pivot on right
            for i in range(l, r):
                if nums[i] <= pivot:
                    swap(i, p)
                    p += 1

            # Place pivot in its final sorted position
            swap(p, r)

            # Now nums[p] is in its correct position
            if p < k:
                return quick_select(p + 1, r)
            elif p > k:
                return quick_select(l, p - 1)
            else:
                return nums[p]

        return quick_select(0, len(nums) - 1)
