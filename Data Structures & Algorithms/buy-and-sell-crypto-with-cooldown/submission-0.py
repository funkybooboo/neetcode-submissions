from typing import List, Dict, Tuple


class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        # { (i, buying): max_profit }
        cache: Dict[Tuple[int, bool], int] = {}

        def dfs(i: int, buying: bool) -> int:
            if i >= len(prices):
                return 0

            if (i, buying) in cache:
                return cache[(i, buying)]

            cooldown = dfs(i + 1, buying)
            if buying:
                buy = dfs(i + 1, not buying) - prices[i]
                cache[(i, buying)] = max(buy, cooldown)
            else:
                sell = dfs(i + 2, not buying) + prices[i]
                cache[(i, buying)] = max(sell, cooldown)

            return cache[(i, buying)]

        return dfs(0, True)
