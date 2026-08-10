from typing import List, Dict


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        permutations: List[List[int]] = []
        current_permutation: List[int] = []
        counts: Dict[int, int] = { n: 0 for n in nums }
        for num in nums:
            counts[num] += 1

        def dfs():
            if len(current_permutation) == len(nums):
                permutations.append(current_permutation.copy())
                return

            for num in counts:
                if counts[num] > 0:
                    current_permutation.append(num)
                    counts[num] -= 1
                    dfs()
                    counts[num] += 1
                    current_permutation.pop()

        dfs()
        return permutations
