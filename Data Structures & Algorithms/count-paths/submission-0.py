from typing import Dict, Tuple


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        cache: Dict[Tuple[int, int], int] = {}

        def dfs(i: int, j: int) -> int:
            nonlocal cache
            if (i, j) in cache:
                return cache[(i, j)]

            if i == m - 1 and j == n - 1:
                return 1

            down_count: int = 0
            if i + 1 <= m - 1:
                down_count = dfs(i + 1, j)

            right_count: int = 0
            if j + 1 <= n - 1:
                right_count = dfs(i, j + 1)

            count: int = down_count + right_count
            cache[(i, j)] = count
            return count

        return dfs(0, 0)
