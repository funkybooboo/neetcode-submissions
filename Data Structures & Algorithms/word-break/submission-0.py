from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        word_set = set(wordDict)  # Faster lookup
        memo = {len(s): True}     # Base case: end of string is always valid

        def can_break(start: int) -> bool:
            if start in memo:
                return memo[start]

            for end in range(start + 1, len(s) + 1):
                word = s[start:end]
                if word in word_set and can_break(end):
                    memo[start] = True
                    return True

            memo[start] = False
            return False

        return can_break(0)
