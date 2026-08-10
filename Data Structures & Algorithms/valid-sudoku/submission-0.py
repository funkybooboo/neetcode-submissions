class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Create sets for rows, columns, and subgrids
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        subgrids = [set() for _ in range(9)]

        for i in range(9):
            for j in range(9):
                num = board[i][j]

                if num == '.':
                    continue  # Skip empty cells

                # Check row validity
                if num in rows[i]:
                    return False
                rows[i].add(num)

                # Check column validity
                if num in cols[j]:
                    return False
                cols[j].add(num)

                # Check subgrid validity
                subgrid_index = (i // 3) * 3 + (j // 3)
                if num in subgrids[subgrid_index]:
                    return False
                subgrids[subgrid_index].add(num)

        return True
