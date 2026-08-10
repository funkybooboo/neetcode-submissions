from typing import List, Set


class Location:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        return f"({self.x}, {self.y})"

    def __hash__(self) -> int:
        return hash(repr(self))


class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        if not mat or not mat[0]:
            return 0

        l1: Location = Location(0, 0)
        l2: Location = Location(len(mat) - 1, 0)
        visited: Set[Location] = set()

        s: int = 0
        while l1.x < len(mat) and l2.x >= 0:
            if hash(l1) not in visited:
                visited.add(hash(l1))
                s += mat[l1.y][l1.x]
            l1.x += 1
            l1.y += 1

            if hash(l2) not in visited:
                visited.add(hash(l2))
                s += mat[l2.y][l2.x]
            l2.x -= 1
            l2.y += 1

        return s
