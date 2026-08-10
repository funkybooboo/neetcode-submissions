from queue import Queue
from typing import List, Tuple, Set

Location = Tuple[int, int]
directions: List[Location] = [(0, 1), (1, 0), (-1, 0), (0, -1)]

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if (
            not image or
            not (1 <= len(image) <= 50) or
            not (1 <= len(image[0]) <= 50) or
            not (0 <= sr < len(image)) or
            not (0 <= sc < len(image[0])) or
            not (0 <= color < 2 ** 16)
        ):
            return []

        start_color = image[sr][sc]
        if start_color == color:
            return image

        def get_neighbors(l: Location) -> List[Location]:
            return list(
                filter(
                    lambda n_l: image[n_l[0]][n_l[1]] == start_color,
                    filter(
                        lambda n_l: (0 <= n_l[0] < len(image)) and (0 <= n_l[1] < len(image[0])),
                        map(
                            lambda d: (d[0] + l[0], d[1] + l[1]),
                            directions
                        )
                    )
                )
            )

        visited: Set[Location] = set()
        queue: Queue[Location] = Queue()
        queue.put((sr, sc))
        while not queue.empty():
            l: Location = queue.get()
            if l in visited:
                continue
            visited.add(l)
            image[l[0]][l[1]] = color
            for n in get_neighbors(l):
                if n not in visited:
                    queue.put(n)

        return image
