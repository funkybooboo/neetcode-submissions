from typing import List, Tuple, Set
import heapq

Loc = Tuple[int ,int]
Direction = Loc

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        if not len(heights) or not len(heights[0]):
            return -1

        rows: int = len(heights)
        columns: int = len(heights[0])
        start: Loc = (0, 0)
        end: Loc = (rows - 1, columns - 1)
        directions: List[Direction] = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        if start == end:
            return 0

        def maximum_absolute_difference(loc1: Loc, loc2: Loc) -> int:
            return abs(heights[loc1[0]][loc1[1]] - heights[loc2[0]][loc2[1]])

        def within_bounds(loc: Loc, direction: Direction) -> bool:
            if 0 <= loc[0] + direction[0] < rows and 0 <= loc[1] + direction[1] < columns:
                return True
            return False

        def get_next_loc(loc: Loc, direction: Direction) -> Loc:
            return loc[0] + direction[0], loc[1] + direction[1]

        # (effort, loc)
        heap: List[Tuple[int, Loc]] = [(0, start)]
        visited: Set[Loc] = set()
        while heap:
            effort, loc = heapq.heappop(heap)

            if loc in visited:
                continue
            visited.add(loc)

            if loc == end:
                return effort

            for direction in directions:
                if not within_bounds(loc, direction):
                    continue
                next_loc: Loc = get_next_loc(loc, direction)
                next_effort: int = maximum_absolute_difference(loc, next_loc)
                heapq.heappush(heap, (max(effort, next_effort), next_loc))

        return -1
