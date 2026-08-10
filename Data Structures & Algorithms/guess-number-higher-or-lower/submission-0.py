class Solution:
    def guessNumber(self, n: int) -> int:
        min: int = 1
        max: int = n

        while True:
            mid: int = (max + min) // 2
            g: int = guess(mid)

            if g > 0:  # too low
                min = mid + 1
            elif g < 0:  # too high
                max = mid - 1
            else:  # got it
                return mid