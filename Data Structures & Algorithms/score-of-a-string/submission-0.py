class Solution:
    def scoreOfString(self, s: str) -> int:
        score: int = 0
        i: int = 0
        while i + 1 < len(s):
            score += abs(ord(s[i]) - ord(s[i + 1]))
            i += 1
        return score
