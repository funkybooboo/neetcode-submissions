from collections import defaultdict
from typing import List, Dict


class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if n < 1 or not trust:
            return -1
        if n == 1 and not trust:
            return 1

        # { who: count }
        in_trust: Dict[int, int] = defaultdict(int)
        out_trust: Dict[int, int] = defaultdict(int)

        for a, b in trust:
            if not (1 <= a <= n) or not (1 <= b <= n):
                return -1
            out_trust[a] += 1
            in_trust[b] += 1

        candidates = [person for person in range(1, n + 1)
                      if in_trust[person] == n - 1 and out_trust[person] == 0]

        return candidates[0] if len(candidates) == 1 else -1
