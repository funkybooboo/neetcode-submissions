from typing import Dict, Tuple


class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        if not s or not t:
            return 0

        cache: Dict[Tuple[int, int], int] = {}

        def dfs(i: int, j: int) -> int:
            if j >= len(t):
                return 1
            if i >= len(s):
                return 0

            if (i, j) in cache:
                return cache[(i, j)]

            a = dfs(i + 1, j)
            b = 0
            if s[i] == t[j]:
                b = dfs(i + 1, j + 1)

            cache[(i, j)] = a + b
            return cache[(i, j)]

        return dfs(0, 0)
