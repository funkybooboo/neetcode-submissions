from typing import List

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        current_sum = 0
        sum_count = {0: 1}

        for num in nums:
            current_sum += num

            if (current_sum - k) in sum_count:
                count += sum_count[current_sum - k]

            if current_sum in sum_count:
                sum_count[current_sum] += 1
            else:
                sum_count[current_sum] = 1

        return count
