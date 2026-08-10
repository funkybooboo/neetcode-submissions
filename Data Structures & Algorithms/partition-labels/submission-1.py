from typing import List, Dict

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        n = len(s)
        if n == 0:
            return []
        if n == 1:
            return [1]

        # Step 1: Record the last occurrence of each character
        last_occurrence: Dict[str, int] = {}
        for i, c in enumerate(s):
            last_occurrence[c] = i

        parts: List[int] = []
        start = 0  # The start index of the current partition
        end = 0    # The farthest index we need to reach in the current partition

        # Step 2: Iterate through the string and create partitions
        for i, c in enumerate(s):
            end = max(end, last_occurrence[c])  # Extend the current partition to cover the last occurrence of the character
            if i == end:  # When we reach the end of the current partition
                parts.append(i - start + 1)  # The size of the partition
                start = i + 1  # Start a new partition

        return parts
