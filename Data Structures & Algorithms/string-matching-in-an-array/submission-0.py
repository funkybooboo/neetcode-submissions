from typing import List

class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        if len(words) == 0 or len(words) == 1:
            return []

        substrings: List[str] = []

        for i, w1 in enumerate(words):
            for j, w2 in enumerate(words):
                if i == j:
                    continue

                if w1 in w2:
                    substrings.append(w1)
                    break


        return substrings
