from collections import deque
from typing import List

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # This will hold the result of the maximum values in each window
        result = []

        # Deque to store the indices of the elements in the current sliding window
        queue = deque()

        # Left and right pointers representing the sliding window
        l = 0
        r = 0

        # Loop through the array until the right pointer reaches the end
        while r < len(nums):
            # Remove elements from the back of the deque that are smaller than the current element
            # This ensures the deque always stores the indices of elements in decreasing order
            while queue and nums[queue[-1]] < nums[r]:
                queue.pop()

            # Add the current element's index to the deque
            queue.append(r)

            # If the left pointer is beyond the element at the front of the deque, remove it
            # This ensures that the deque always contains the elements within the current window
            if l > queue[0]:
                queue.popleft()

            # If the current window has reached the size k, we add the maximum value to the result
            if (r + 1) >= k:
                # The element at the front of the deque is the maximum in the current window
                result.append(nums[queue[0]])

                # Move the left pointer to shrink the window
                l += 1

            # Move the right pointer to expand the window
            r += 1

        # Return the list of maximum values for each sliding window
        return result
