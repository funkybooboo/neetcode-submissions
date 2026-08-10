from typing import List


class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        if len(triplets) == 0 or len(target) == 0:
            return True
        if len(triplets) == 0:
            return False
        if len(target) == 0:
            return False
        if len(triplets[0]) != 3:
            return False

        result = []
        for triplet in triplets:
            if triplet[0] > target[0] or triplet[1] > target[1] or triplet[2] > target[2]:
                continue
            if len(result) == 0:
                result = triplet
            else:
                result = [max(triplet[0], result[0]), max(triplet[1], result[1]), max(triplet[2], result[2])]

        return len(result) == 3 and result[0] == target[0] and result[1] == target[1] and result[2] == target[2]
