from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if not digits:
            return []

        r: List[int] = []
        carry: bool = True

        for i in range(len(digits) - 1, -1, -1):
            d: int = digits[i]

            if carry:
                if d + 1 == 10:
                    d = 0
                    carry = True
                else:
                    d += 1
                    carry = False

            r.append(d)

        if carry:
            r.append(1)

        return list(reversed(r))
