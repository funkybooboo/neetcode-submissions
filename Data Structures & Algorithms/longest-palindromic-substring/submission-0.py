class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expandAroundCenter(left: int, right: int) -> str:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            # Return the expanded palindrome substring
            return s[left + 1:right]

        longest = ""

        for i in range(len(s)):
            # Expand around single center (odd length)
            odd = expandAroundCenter(i, i)
            # Expand around double center (even length)
            even = expandAroundCenter(i, i + 1)

            # Choose the longer palindrome
            longer = odd if len(odd) > len(even) else even
            if len(longer) > len(longest):
                longest = longer

        return longest
