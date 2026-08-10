from typing import List, Dict

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counts: Dict[int, int] = {} # { number: count }

        for num in nums:
            if num in counts:
                counts[num] += 1
            else:
                counts[num] = 1

        max_num: int = -1
        max_count: int = -1
        for num, count in counts.items():
            if count > max_count:
                max_count = count
                max_num = num

        return max_num
