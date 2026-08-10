from typing import List

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1 = sorted(s1)

        for i in range(len(s2)):
            for j in range(i, len(s2)):
                sub_str = s2[i : j + 1]
                sub_str = sorted(sub_str)
                if sub_str == s1:
                    return True
        return False
