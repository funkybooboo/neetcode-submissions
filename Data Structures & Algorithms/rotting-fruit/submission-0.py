from collections import deque
from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()  # Queue to perform BFS from all initially rotten oranges
        fresh = 0  # Counter for the number of fresh oranges
        time = 0  # Tracks the time (in minutes) it takes for oranges to rot

        # Step 1: Count fresh oranges and enqueue positions of rotten oranges
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    fresh += 1  # Found a fresh orange
                elif grid[r][c] == 2:
                    q.append((r, c))  # Found a rotten orange; enqueue it

        # All four possible 4-directional moves: right, left, down, up
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        # Step 2: BFS from rotten oranges, each layer = 1 minute
        while fresh > 0 and q:
            length = len(q)
            for _ in range(length):
                r, c = q.popleft()

                for dr, dc in directions:
                    row, col = r + dr, c + dc
                    # Check if the new position is in bounds and contains a fresh orange
                    if (0 <= row < len(grid) and
                            0 <= col < len(grid[0]) and
                            grid[row][col] == 1):
                        # Rot the fresh orange
                        grid[row][col] = 2
                        q.append((row, col))
                        fresh -= 1  # Decrement fresh orange count

            time += 1  # One round of rotting completed (1 minute)

        # Step 3: If all oranges are rotten, return time; otherwise, return -1
        return time if fresh == 0 else -1
