class Solution:
    def reverse(self, x: int) -> int:
        limit: int = 2147483647
        s = str(x)
        r = ''
        n = False
        for c in reversed(s):
            if c == "-":
                n = True
                continue
            r += c

        r = int(r)
        if n:
            r *= -1

        if -limit < r < limit:
            return r
        else:
            return 0



Solution().reverse(12)

