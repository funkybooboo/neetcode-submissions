from typing import Dict, Tuple


class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False

        cache: Dict[Tuple[int, int], bool] = {}

        def dfs(i1: int, i2: int) -> bool:
            if i1 == len(s1) and i2 == len(s2):
                return True

            if (i1, i2) in cache:
                return cache[(i1, i2)]

            i3: int = i1 + i2

            if i1 < len(s1) and s1[i1] == s3[i3] and dfs(i1 + 1, i2):
                cache[(i1, i2)] = True
                return cache[(i1, i2)]

            if i2 < len(s2) and s2[i2] == s3[i3] and dfs(i1, i2 + 1):
                cache[(i1, i2)] = True
                return cache[(i1, i2)]

            cache[(i1, i2)] = False
            return cache[(i1, i2)]

        return dfs(0, 0)
