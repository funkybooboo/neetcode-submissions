from typing import List

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        """
        Solve the N-Queens problem for an n×n board.
        Returns a list of all distinct solutions, where each solution
        is represented as a list of strings ('.' for empty, 'Q' for queen).
        """
        solutions: List[List[str]] = []

        # Initialize an empty board: a 2D list of '.' characters
        board: List[List[str]] = [["."] * n for _ in range(n)]

        def backtrack(current_row: int) -> None:
            """
            Try to place a queen on each column of `current_row`, then
            recurse to the next row. When `current_row == n`, we've
            placed n queens successfully and can record the solution.
            """
            nonlocal n

            # If we've placed queens on all rows, record the current board
            if current_row == n:
                solution = ["".join(row) for row in board]
                solutions.append(solution)
                return

            # Attempt to place a queen in each column of this row
            for current_col in range(n):
                if self._is_safe_position(current_row, current_col, board):
                    # Place the queen
                    board[current_row][current_col] = "Q"
                    # Recurse to place the next queen
                    backtrack(current_row + 1)
                    # Remove the queen (backtrack)
                    board[current_row][current_col] = "."

        # Kick off the backtracking from row 0
        backtrack(0)
        return solutions

    @staticmethod
    def _is_safe_position(row: int, col: int, board: List[List[str]]) -> bool:
        """
        Check if it's safe to place a queen at (row, col). A position is
        safe if no other queen attacks it vertically or along either diagonal.
        """
        size = len(board)

        # 1) Check the same column above the current row
        for r in range(row):
            if board[r][col] == "Q":
                return False

        # 2) Check the upper-left diagonal
        r, c = row - 1, col - 1
        while r >= 0 and c >= 0:
            if board[r][c] == "Q":
                return False
            r -= 1
            c -= 1

        # 3) Check the upper-right diagonal
        r, c = row - 1, col + 1
        while r >= 0 and c < size:
            if board[r][c] == "Q":
                return False
            r -= 1
            c += 1

        # No conflicts found; the position is safe
        return True
