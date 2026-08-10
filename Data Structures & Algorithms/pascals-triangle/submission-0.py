from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle: List[List[int]] = []

        if numRows <= 0:
            return triangle

        triangle.append([1])
        if numRows == 1:
            return triangle

        triangle.append([1, 1])
        if numRows == 2:
            return triangle

        for level in range(2, numRows):
            row: List[int] = [1]
            for i in range(1, level):
                v: int = triangle[level - 1][i - 1] + triangle[level - 1][i]
                row.append(v)
            row.append(1)
            triangle.append(row)

        return triangle
