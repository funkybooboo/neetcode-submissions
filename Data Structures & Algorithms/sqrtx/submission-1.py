class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 0:
            return -1
        if x == 0:
            return 0
        if x == 1:
            return 1

        l: int = 0
        r: int = x

        while l <= r:
            m: int = (l + r) // 2
            s: int = m * m
            if s == x:
                return m
            elif s < x:
                l = m + 1
            else: # s > x:
                r = m - 1

        return r
