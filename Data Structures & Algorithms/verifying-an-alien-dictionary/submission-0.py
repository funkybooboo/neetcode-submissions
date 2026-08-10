from typing import List, Dict


class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        if len(words) == 0 or len(words) == 1:
            return True

        order_m: Dict[str, int] = {}
        for i, l in enumerate(order):
            order_m[l] = i

        for i in range(len(words) - 1):
            word1: str = words[i]
            word2: str = words[i + 1]

            max_len: int = min(len(word1), len(word2))
            for j in range(max_len):
                l1: str = word1[j]
                l2: str = word2[j]
                o1: int = order_m[l1]
                o2: int = order_m[l2]
                if o1 == o2:
                    continue
                if o1 < o2:
                    break
                return False
            else:
                if len(word1) > len(word2):
                    return False

        return True
