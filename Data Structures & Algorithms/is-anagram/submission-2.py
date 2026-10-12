class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        if not s and not t:
            return False

        s_m: dict[str, int] = {}  # { char : count }
        t_m: dict[str, int] = {}  # { char : count }

        for c in s:
            if c in s_m:
                s_m[c] += 1
            else:
                s_m[c] = 1

        for c in t:
            if c in t_m:
                t_m[c] += 1
            else:
                t_m[c] = 1

        for k, v in s_m.items():
            if k not in t_m:
                return False
            if v != t_m[k]:
                return False

        for k, v in t_m.items():
            if k not in s_m:
                return False
            if v != s_m[k]:
                return False

        return True