from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        if len(s) == 0 or len(s) == 1:
            return
        
        l: int = 0
        r: int = len(s) - 1
        
        while l < r:
            t = s[r]
            s[r] = s[l]
            s[l] = t
            l += 1
            r -= 1
