from typing import List, Set, Tuple

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        """
        Return True if `word` can be formed by sequentially adjacent letters
        in `board`, where adjacent cells are horizontally or vertically
        neighboring. Each cell may be used only once per word search.
        """
        # Number of rows and columns in the board
        num_rows, num_cols = len(board), len(board[0])
        # Keep track of which cells are part of the current search path
        visited: Set[Tuple[int, int]] = set()

        def dfs(row: int, col: int, index: int) -> bool:
            """
            Depth-first search from (row, col) to match word[index:].
            Returns True if the substring word[index:] can be found starting
            at this cell.
            """
            # If we've matched all characters in word, we succeed
            if index == len(word):
                return True

            # Check for out-of-bounds, character mismatch, or revisiting
            if (row < 0 or row >= num_rows or
                col < 0 or col >= num_cols or
                board[row][col] != word[index] or
                (row, col) in visited):
                return False

            # Mark this cell as visited in the current path
            visited.add((row, col))

            # Explore all four directions: down, up, right, left
            found = (
                dfs(row + 1, col, index + 1) or
                dfs(row - 1, col, index + 1) or
                dfs(row, col + 1, index + 1) or
                dfs(row, col - 1, index + 1)
            )

            # Backtrack: remove the cell from the current path
            visited.remove((row, col))
            return found

        # Try starting the DFS from every cell in the grid
        for r in range(num_rows):
            for c in range(num_cols):
                # If the first letter matches, start a DFS from here
                if dfs(r, c, 0):
                    return True

        # If no starting point yields the full word, return False
        return False
