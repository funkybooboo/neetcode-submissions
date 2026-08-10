class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        # Step 1: Remove duplicates by converting to a set
        nums = set(nums)

        # Step 2: Add all unique elements to the min heap
        min_heap = []
        for num in nums:
            heapq.heappush(min_heap, num)

        # Step 3: Find the longest consecutive sequence
        longest_streak = 1
        current_streak = 1
        prev_num = heapq.heappop(min_heap)  # Pop the smallest element from the heap

        while min_heap:
            current_num = heapq.heappop(min_heap)  # Pop the next smallest element

            # Step 4: Check if the current number is consecutive
            if current_num == prev_num + 1:
                current_streak += 1
            else:
                # Update longest streak if the current streak is longer
                longest_streak = max(longest_streak, current_streak)
                current_streak = 1  # Reset streak to 1

            prev_num = current_num

        # Final check to account for the last streak
        longest_streak = max(longest_streak, current_streak)

        return longest_streak