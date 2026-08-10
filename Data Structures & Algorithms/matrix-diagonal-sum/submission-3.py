from typing import List


class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        if not mat or not mat[0]:
            return 0

        x1: int = 0
        y1: int = 0
        x2: int = len(mat) - 1
        y2: int = 0

        s: int = 0
        while x1 < len(mat) and x2 >= 0:
            s += mat[y1][x1]

            if not (x1 == x2 and y1 == y2):
                s += mat[y2][x2]

            x1 += 1
            y1 += 1
            x2 -= 1
            y2 += 1

        return s
