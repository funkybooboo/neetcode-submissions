from typing import List, Dict, Tuple
from collections import defaultdict
import heapq

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) == 0 or groupSize < 1 or len(hand) % groupSize != 0:
            return False
        if groupSize == 1:
            return True

        hand.sort()

        # This dict tracks how many groups are waiting for a specific next number
        looking_for: Dict[int, List[int]] = defaultdict(list)  # number_wanted -> list of group sizes so far

        for card in hand:
            if looking_for[card]:
                # Continue an existing group
                current_size = heapq.heappop(looking_for[card])
                next_size = current_size + 1
                if next_size < groupSize:
                    heapq.heappush(looking_for[card + 1], next_size)
                # Else, group is complete, do nothing
            else:
                # Start a new group from this card
                heapq.heappush(looking_for[card + 1], 1)  # we've used 1 card so far

        # If all groups are completed, no group should be left waiting
        return all(len(q) == 0 for q in looking_for.values())
