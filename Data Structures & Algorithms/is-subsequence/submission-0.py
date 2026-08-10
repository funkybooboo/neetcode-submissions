class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0 and len(t) == 0:
            return True
        if len(t) == 0:
            return False
        if len(s) == 0:
            return True
        if len(s) > len(t):
            return False
        if len(s) == len(t):
            return s == t

        i: int = 0
        j: int = 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1

        return i == len(s)
