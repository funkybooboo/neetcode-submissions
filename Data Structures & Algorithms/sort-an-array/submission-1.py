from typing import List
import random

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums

        def swap(a: List[int], i: int, j: int) -> None:
            a[i], a[j] = a[j], a[i]

        def insertion_sort(a: List[int], lo: int, hi: int) -> None:
            # inclusive hi
            for i in range(lo + 1, hi + 1):
                key = a[i]
                j = i - 1
                while j >= lo and a[j] > key:
                    a[j + 1] = a[j]
                    j -= 1
                a[j + 1] = key

        def choose_pivot_and_move_to_end(a: List[int], lo: int, hi: int) -> None:
            # median-of-three pivot selection
            mid = lo + ((hi - lo) >> 1)
            trio = [(a[lo], lo), (a[mid], mid), (a[hi], hi)]
            trio.sort(key=lambda x: x[0])
            _, median_idx = trio[1]
            swap(a, median_idx, hi)

        def partition(a: List[int], lo: int, hi: int) -> int:
            # Lomuto partition with pivot at a[hi]
            pivot = a[hi]
            i = lo
            for j in range(lo, hi):
                if a[j] < pivot:
                    swap(a, i, j)
                    i += 1
            swap(a, i, hi)
            return i

        # iterative quicksort using an explicit stack of (lo, hi) inclusive
        stack: List[tuple[int, int]] = [(0, len(nums) - 1)]
        INSERTION_CUTOFF = 16

        while stack:
            lo, hi = stack.pop()
            if lo >= hi:
                continue

            # use insertion sort for small partitions
            if hi - lo + 1 <= INSERTION_CUTOFF:
                insertion_sort(nums, lo, hi)
                continue

            # randomized shuffle small chance plus median-of-three to avoid worst-case
            # occasionally swap a random element into hi to further reduce pattern risks
            if random.random() < 0.02:
                swap(nums, hi, random.randint(lo, hi))

            choose_pivot_and_move_to_end(nums, lo, hi)
            p = partition(nums, lo, hi)

            # push larger partition first to keep stack small
            left_size = p - 1 - lo
            right_size = hi - (p + 1)
            if left_size > right_size:
                if lo < p - 1:
                    stack.append((lo, p - 1))
                if p + 1 < hi:
                    stack.append((p + 1, hi))
            else:
                if p + 1 < hi:
                    stack.append((p + 1, hi))
                if lo < p - 1:
                    stack.append((lo, p - 1))

        return nums
