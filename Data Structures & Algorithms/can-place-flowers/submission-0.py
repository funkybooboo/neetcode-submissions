from typing import List

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n < 0:
            return False
        if n == 0:
            return True
        if len(flowerbed) == 0:
            return False
        if len(flowerbed) < n:
            return False

        flowers: int = 0
        for plot in flowerbed:
            if plot == 1:
                flowers += 1
        if len(flowerbed) - flowers < n:
            return False

        def nehbors_are_empty(i: int) -> bool:
            left_empty = (i == 0) or (flowerbed[i - 1] == 0)
            right_empty = (i == len(flowerbed) - 1) or (flowerbed[i + 1] == 0)
            return left_empty and right_empty

        count: int = n

        for i in range(len(flowerbed)):
            if flowerbed[i] == 0 and nehbors_are_empty(i):
                flowerbed[i] = 1
                count -= 1
                if count == 0:
                    return True

        return False