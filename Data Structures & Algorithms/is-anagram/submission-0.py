class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s = s.replace(" ", "")
        t = t.replace(" ", "")

        if len(s) != len(t):
            return False

        sm: Dict[str, int] = {}
        tm: Dict[str, int] = {}

        for c in s:
            sm[c] = sm.get(c, 0) + 1

        for c in t:
            tm[c] = tm.get(c, 0) + 1

        return sm == tm
