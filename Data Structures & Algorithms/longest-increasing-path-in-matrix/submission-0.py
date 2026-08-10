from typing import List


class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix or not matrix[0]:
            return 0

        m, n = len(matrix), len(matrix[0])
        cache = [[0 for _ in range(n)] for _ in range(m)]
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        def dfs(x: int, y: int) -> int:
            if cache[x][y]:
                return cache[x][y]

            longest = 1
            for dx, dy in dirs:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and matrix[nx][ny] > matrix[x][y]:
                    longest = max(longest, dfs(nx, ny) + 1)
            cache[x][y] = longest
            return longest

        max_longest: int = 0
        for x in range(m):
            for y in range(n):
                max_longest = max(dfs(x, y), max_longest)

        return max_longest
