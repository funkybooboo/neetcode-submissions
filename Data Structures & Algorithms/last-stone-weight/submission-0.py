from typing import List

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if not stones:
            return 0

        while len(stones) > 1:
            stones.sort()
            x = stones.pop()   # heaviest
            y = stones.pop()   # second heaviest

            if x != y:
                stones.append(x - y)

        return stones[0] if stones else 0
