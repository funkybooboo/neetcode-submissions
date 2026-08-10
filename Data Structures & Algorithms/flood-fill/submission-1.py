from queue import Queue
from typing import List, Tuple, Set

Location = Tuple[int, int]
DIRECTIONS: List[Location] = [(0, 1), (1, 0), (-1, 0), (0, -1)]


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if not image or not image[0]:
            return image

        rows, cols = len(image), len(image[0])
        if not (0 <= sr < rows and 0 <= sc < cols):
            return image

        start_color = image[sr][sc]
        if start_color == color:
            return image  # No change needed

        # Queue for BFS
        queue: Queue[Location] = Queue()
        queue.put((sr, sc))
        visited: Set[Location] = set()
        
        while not queue.empty():
            r, c = queue.get()
            if (r, c) in visited:
                continue
            visited.add((r, c))

            # Recolor current pixel
            image[r][c] = color

            # Explore valid neighbors with the same starting color
            for dr, dc in DIRECTIONS:
                nr, nc = r + dr, c + dc
                if (
                    0 <= nr < rows and
                    0 <= nc < cols and
                    image[nr][nc] == start_color and
                    (nr, nc) not in visited
                ):
                    queue.put((nr, nc))

        return image
