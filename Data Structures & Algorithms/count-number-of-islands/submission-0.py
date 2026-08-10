from typing import List

class Solution:
    """
    Count the number of islands in a 2D grid of '1's (land) and '0's (water).
    We use a DFS flood-fill approach to 'sink' each discovered island so it's
    not counted more than once.
    """
    def numIslands(self, grid: List[List[str]]) -> int:
        """
        Given a 2D grid map of '1's (land) and '0's (water), return the number
        of islands. An island is surrounded by water and is formed by
        connecting adjacent lands horizontally or vertically.

        This implementation modifies the grid in place: each visited land cell
        is flipped from '1' to '0' to mark it as seen.

        Time complexity: O(M×N), where M and N are grid dimensions.
        Space complexity: O(M×N) in the worst case (DFS recursion).
        """
        # Handle edge case: empty grid
        if not grid or not grid[0]:
            return 0

        # Dimensions of the grid
        rows = len(grid)
        cols = len(grid[0])

        # Four possible directions: down, up, right, left
        directions = [
            (1, 0),    # down
            (-1, 0),   # up
            (0, 1),    # right
            (0, -1),   # left
        ]

        # Number of islands found
        island_count = 0

        def dfs(r: int, c: int) -> None:
            """
            Depth-first search to visit and mark all cells in the current island.
            Stops when it hits water ('0') or goes out of bounds.
            """
            # Check boundaries and whether this cell is water already
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] != '1':
                return

            # Mark current cell as visited by sinking it to '0'
            grid[r][c] = '0'

            # Recursively visit all neighboring cells
            for dr, dc in directions:
                dfs(r + dr, c + dc)

        # Iterate over every cell in the grid
        for r in range(rows):
            for c in range(cols):
                # If we find land, it's a new island
                if grid[r][c] == '1':
                    dfs(r, c)        # Sink the entire island
                    island_count += 1  # Increment our island counter

        return island_count
