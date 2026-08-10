from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount < 0:
            return -1
        if amount == 0:
            return 0
        if not coins:
            return -1

        memo = {}

        def dfs(remaining: int) -> int:
            if remaining in memo:
                return memo[remaining]
            if remaining == 0:
                return 0
            if remaining < 0:
                return -1

            min_coins = float('inf')
            for coin in coins:
                result = dfs(remaining - coin)
                if result >= 0:
                    min_coins = min(min_coins, result + 1)

            memo[remaining] = -1 if min_coins == float('inf') else min_coins
            return memo[remaining]

        return dfs(amount)
