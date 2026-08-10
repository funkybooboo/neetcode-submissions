import heapq
from collections import defaultdict
from typing import List, Tuple

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        # Helper function to create a node with height
        def make_node(point: Tuple[int, int], height: int = -1) -> Tuple[int, int, int]:
            x, y = point
            if height == -1:
                height = grid[x][y]
            return height, x, y

        # Helper function to split a node into height and point
        def split_node(node: Tuple[int, int, int]) -> Tuple[int, Tuple[int, int]]:
            return node[0], (node[1], node[2])

        # Helper function to get the height of a point
        def get_height(point: Tuple[int, int]) -> int:
            return grid[point[0]][point[1]]

        n = len(grid)
        source = (0, 0)
        sink = (n - 1, n - 1)

        # Handle edge cases
        if n == 0:
            return 0
        if n == 1:
            return grid[0][0]

        # Create the adjacency list
        adj_list = defaultdict(list)
        for i in range(n):
            for j in range(n):
                if i > 0:  # Up
                    adj_list[(i, j)].append((i - 1, j))
                if j < n - 1:  # Right
                    adj_list[(i, j)].append((i, j + 1))
                if i < n - 1:  # Down
                    adj_list[(i, j)].append((i + 1, j))
                if j > 0:  # Left
                    adj_list[(i, j)].append((i, j - 1))

        # Initialize the min-heap with the source node
        min_heap = []
        heapq.heappush(min_heap, make_node(source))
        visited = set()

        # Perform BFS using the min-heap
        while True:
            height, point = split_node(heapq.heappop(min_heap))
            visited.add(point)
            if point == sink:
                return height

            # Explore neighbors
            neighbors = adj_list[point]
            for neighbor in neighbors:
                if neighbor not in visited:
                    new_height = max(height, get_height(neighbor))
                    heapq.heappush(min_heap, make_node(neighbor, new_height))
