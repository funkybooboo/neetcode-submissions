class Solution:
    def isPalindrome(self, s: str) -> bool:
        # clean up
        s = s.lower()
        s.replace(" ", "")
        n_s = ""
        for c in s:
            if c.isalnum():
                n_s += c
        s = n_s

        # two pointers
        l = 0
        r = len(s) - 1
        while l <= r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True
