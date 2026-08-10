from typing import Set


class Solution:
    def isHappy(self, n: int) -> bool:
        seen: Set[int] = set()

        r = n
        while True:
            s = str(r)
            r = 0
            for c in s:
                r += int(c) ** 2

            if r == 1:
                return True

            if r in seen:
                return False
            seen.add(r)
