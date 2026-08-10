from typing import Dict

INF: int = 1000000000

class Solution:
    def maxDifference(self, s: str) -> int:
        freqs: Dict[str, int] = {} # { char: count }
        for c in s:
            freqs[c] = freqs.get(c, 0) + 1

        biggest_odd_freq: int = -INF
        smallest_even_freq: int = INF
        for count in freqs.values():
            if count % 2 == 0:
                smallest_even_freq = min(smallest_even_freq, count)
            else:
                biggest_odd_freq = max(biggest_odd_freq, count)

        if biggest_odd_freq == -INF:
            biggest_odd_freq = 0
        if smallest_even_freq == INF:
            smallest_even_freq = 0

        return biggest_odd_freq - smallest_even_freq
