from typing import List

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        meno = [0] * (n + 1)  # meno[i] = min cost to reach step i

        for i in range(2, n + 1):
            meno[i] = min(
                meno[i - 1] + cost[i - 1],
                meno[i - 2] + cost[i - 2]
            )

        return meno[n]
