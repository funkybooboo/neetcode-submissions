import heapq
from typing import List

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Step 1: Create a min-heap with the first k elements
        min_heap = nums[:k]
        heapq.heapify(min_heap)  # turns the list into a valid min-heap

        # Step 2: For each remaining number, if it's bigger than the smallest in heap, replace it
        for num in nums[k:]:
            if num > min_heap[0]:  # only replace if the number is larger
                heapq.heappushpop(min_heap, num)  # push new num and pop the smallest

        # Step 3: The root of the heap is the kth largest element
        return min_heap[0]

# Example usage:
if __name__ == "__main__":
    print(Solution().findKthLargest([1, 4, 3, 1, 4, 5, 3], 2))  # Output: 4
