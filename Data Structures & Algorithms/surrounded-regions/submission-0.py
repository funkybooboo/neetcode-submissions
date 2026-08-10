from typing import List

class DisjointSetUnion:
    """Union-Find (DSU) with path compression and union by size."""
    def __init__(self, n: int):
        # parent[i] points to the parent of i; root nodes point to themselves
        self.parent = list(range(n))
        # size[i] tracks the size of the tree rooted at i
        self.size = [1] * n

    def find(self, x: int) -> int:
        """Finds and returns the root of x, compressing path along the way."""
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x: int, y: int) -> bool:
        """
        Unites the sets containing x and y.
        Returns True if a merge happened, False if already in the same set.
        """
        rx, ry = self.find(x), self.find(y)
        if rx == ry:
            return False
        # Attach smaller tree under the larger one
        if self.size[rx] < self.size[ry]:
            rx, ry = ry, rx
        self.parent[ry] = rx
        self.size[rx] += self.size[ry]
        return True

    def connected(self, x: int, y: int) -> bool:
        """Checks if x and y are in the same set."""
        return self.find(x) == self.find(y)


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Flip all 'O's that are completely surrounded by 'X' into 'X'.
        Any 'O' connected (directly or indirectly) to the border remains 'O'.
        """
        if not board or not board[0]:
            return  # empty board, nothing to do

        rows, cols = len(board), len(board[0])

        def node_id(r: int, c: int) -> int:
            """Map 2D coordinates to 1D DSU index."""
            return r * cols + c

        total_cells = rows * cols
        dummy = total_cells  # extra node representing the “border”
        dsu = DisjointSetUnion(total_cells + 1)

        # 4-directional neighbors (up/down/left/right)
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        # 1) Union pass: connect border-touching 'O's to dummy, 
        #    and union adjacent 'O's internally.
        for r in range(rows):
            for c in range(cols):
                if board[r][c] != 'O':
                    continue

                curr = node_id(r, c)

                # If on the border, unite with dummy
                if r == 0 or c == 0 or r == rows - 1 or c == cols - 1:
                    dsu.union(curr, dummy)

                # Unite with any adjacent 'O's
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] == 'O':
                        dsu.union(curr, node_id(nr, nc))

        # 2) Flip pass: any 'O' not connected to dummy is surrounded -> flip it.
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'O' and not dsu.connected(node_id(r, c), dummy):
                    board[r][c] = 'X'
