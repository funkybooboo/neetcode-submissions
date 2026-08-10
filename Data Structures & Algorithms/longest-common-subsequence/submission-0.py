from typing import List


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if len(text1) == 0 or len(text2) == 0:
            return 0

        # match -> i + 1 j + 1
        # dont match -> i + 1 and j + 1
        #   a c e
        # a 1
        # b   x x
        # c   1
        # d     x
        # e     1

        grid: List[List[int]] = [[0 for _ in range(len(text2) + 1)] for _ in range(len(text1) + 1)]

        for i in range(len(text1) - 1, -1, -1):
            for j in range(len(text2) - 1, -1, -1):
                if text1[i] == text2[j]:
                    grid[i][j] = 1 + grid[i + 1][j + 1]
                else:
                    grid[i][j] = max(grid[i][j + 1], grid[i + 1][j])

        return grid[0][0]
