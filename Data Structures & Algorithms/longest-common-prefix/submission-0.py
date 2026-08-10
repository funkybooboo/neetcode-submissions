from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        if len(strs) == 1:
            return strs[0]

        for s in strs:
            if not s:
                return ""

        shortest_str_len = min(len(s) for s in strs)
        shortest_str_idx = min(range(len(strs)), key=lambda i: len(strs[i]))

        prefix: str = ""
        while len(prefix) < shortest_str_len:
            i: int = len(prefix)
            c: str = strs[shortest_str_idx][i]
            for s in strs:
                if s[i] != c:
                    return prefix
            prefix += c

        return prefix
