from typing import List, Tuple, Set


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        # find 0s locations
        locs: Set[Tuple[int, int]] = set() # [(x, y)]
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if matrix[row][col] == 0:
                    locs.add((row, col))

        # calc what rows and columns need to be set
        rows: Set[int] = set()
        cols: Set[int] = set()
        for row, col in locs:
            t = col
            if not row in rows:
                for col in range(len(matrix[row])):
                    matrix[row][col] = 0
                rows.add(row)

            col = t
            if not col in cols:
                for row in range(len(matrix)):
                    matrix[row][col] = 0
                cols.add(col)
