from typing import List, Dict


class Solution:
    def jump(self, nums: List[int]) -> int:
        big_num = 1000000
        cache: Dict[int, int] = {}

        def dfs(i: int) -> int:
            if i in cache:
                return cache[i]
            if i == len(nums) - 1:
                return 0
            if nums[i] == 0:
                return big_num

            r: int = big_num
            end: int = min(len(nums), i + nums[i] + 1)
            for j in range(i + 1, end):
                r = min(r, dfs(j) + 1)
            cache[i] = r
            return r

        r = dfs(0)
        return r if r != big_num else 0
