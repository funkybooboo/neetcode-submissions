from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # Sort candidates so we can stop early when candidates[j] > remaining
        candidates.sort()
        result: List[List[int]] = []
        combination: List[int] = []

        def helper(remaining: int, start_index: int):
            # If we've hit exactly zero, record a copy of the combination
            if remaining == 0:
                result.append(combination.copy())
                return
            # If we overshot, stop exploring this path
            if remaining < 0:
                return

            # Try each candidate from start_index onward
            for j in range(start_index, len(candidates)):
                candidate = candidates[j]
                # If candidate exceeds what remains, no need to continue further
                if candidate > remaining:
                    break

                # Include this candidate
                combination.append(candidate)
                # Recurse with updated remaining; j (not j+1) allows reuse
                helper(remaining - candidate, j)
                # Remove last element and try the next candidate
                combination.pop()

        # Kick off backtracking with the full target and starting at index 0
        helper(target, 0)
        return result
