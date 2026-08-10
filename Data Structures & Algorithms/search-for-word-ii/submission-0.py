from typing import List

class Node:
    def __init__(self):
        self.children: dict[str, Node] = {}
        self.is_word = False

    def addWord(self, word: str):
        current = self
        for char in word:
            if char not in current.children:
                current.children[char] = Node()
            current = current.children[char]
        current.is_word = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = Node()

        for word in words:
            root.addWord(word)

        ROWS, COLS = len(board), len(board[0])
        result, visited = set(), set()

        def helper(r: int, c: int, node: Node, word: str):
            if (
                    r < 0 or
                    c < 0 or
                    r == ROWS or
                    c == COLS or
                    (r, c) in visited or
                    board[r][c] not in node.children
            ):
                return

            visited.add((r, c))
            node = node.children[board[r][c]]
            word += board[r][c]
            if node.is_word:
                result.add(word)

            helper(r - 1, c, node, word)
            helper(r + 1, c, node, word)
            helper(r, c - 1, node, word)
            helper(r, c + 1, node, word)

            visited.remove((r, c))

        for r in range(ROWS):
            for c in range(COLS):
                helper(r, c, root, "")

        return list(result)
