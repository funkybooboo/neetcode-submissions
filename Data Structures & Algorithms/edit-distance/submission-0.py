from typing import Dict, Tuple


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m: int = len(word1)
        n: int = len(word2)
        cache: Dict[Tuple[int, int], int] = {}

        def dfs(i: int, j: int) -> int:
            if (i, j) in cache:
                return cache[(i, j)]

            if i == m:
                return n - j # insert remaining word2
            if j == n:
                return m - i # delete remaining word1

            if word1[i] == word2[j]:
                a = dfs(i + 1, j + 1)
            else:
                insert = 1 + dfs(i, j + 1)  # insert word2[j]
                delete = 1 + dfs(i + 1, j)  # delete word1[i]
                replace = 1 + dfs(i + 1, j + 1)  # replace word1[i] with word2[j]
                a = min(insert, delete, replace)

            cache[(i, j)] = a
            return cache[(i, j)]

        return dfs(0, 0)
