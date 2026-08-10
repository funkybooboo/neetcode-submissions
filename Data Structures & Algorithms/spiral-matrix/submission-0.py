from enum import Enum, auto
from typing import List


class Direction(Enum):
    Left = auto()
    Right = auto()
    Up = auto()
    Down = auto()


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        count: int = len(matrix) * len(matrix[0])
        n: int = len(matrix)
        m: int = len(matrix[0])

        spiral_order: List[int] = []
        x: int = 0
        y: int = 0
        direction: Direction = Direction.Right

        max_right: int = m
        max_down: int = n
        min_left: int = 0
        min_up: int = 1

        while len(spiral_order) < count:
            spiral_order.append(matrix[y][x])

            if direction == Direction.Right:
                if x + 1 >= max_right:
                    direction = Direction.Down
                    max_right -= 1
                    y += 1
                else:
                    x += 1
            elif direction == Direction.Down:
                if y + 1 >= max_down:
                    direction = Direction.Left
                    max_down -= 1
                    x -= 1
                else:
                    y += 1
            elif direction == Direction.Left:
                if x - 1 < min_left:
                    direction = Direction.Up
                    min_left += 1
                    y -= 1
                else:
                    x -= 1
            else:  # direction == Direction.Up
                if y - 1 < min_up:
                    direction = Direction.Right
                    min_up += 1
                    x += 1
                else:
                    y -= 1

        return spiral_order
