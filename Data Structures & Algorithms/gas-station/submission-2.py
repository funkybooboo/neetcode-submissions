from typing import List

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if len(gas) == 0 or len(gas) != len(cost):
            return -1

        n = len(gas)

        # build diff and check feasibility
        diff = [0] * n
        total = 0
        for i, (g, c) in enumerate(zip(gas, cost)):
            diff[i] = g - c
            total += diff[i]
        if total < 0:
            return -1

        tank = 0
        right_index = left_index = 0
        steps = 0  # how many stations we've successfully covered from current start

        while steps < n:
            tank += diff[right_index]
            if tank < 0:
                # current start fails; move start to the next station after failure
                left_index = (right_index + 1) % n
                tank = 0
                steps = 0
                right_index = left_index
                continue

            right_index = (right_index + 1) % n
            steps += 1

        return left_index
