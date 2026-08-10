class Solution:
    def countSubstrings(self, s: str) -> int:
        def expandAroundCenter(left: int, right: int) -> int:
            count = 0
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
                count += 1
            return count

        total = 0
        for i in range(len(s)):
            # Expand around single center (odd length)
            total += expandAroundCenter(i, i)
            # Expand around double center (even length)
            total += expandAroundCenter(i, i + 1)
        return total
