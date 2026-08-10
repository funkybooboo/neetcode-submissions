from typing import List


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        if not coins:
            return 0

        cache: List[List[int]] = [[0] * (len(coins) + 1) for _ in range(amount + 1)]
        cache[0] = [1] * (len(coins) + 1)

        for a in range(1, amount + 1):
            for i in range(len(coins) - 1, -1 , -1):
                cache[a][i] = cache[a][i + 1]
                if a - coins[i] >= 0:
                    cache[a][i] += cache[a - coins[i]][i]

        return cache[amount][0]
