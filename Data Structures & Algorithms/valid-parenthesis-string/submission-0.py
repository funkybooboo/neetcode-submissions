class Solution:
    def checkValidString(self, s: str) -> bool:
        if len(s) == 0:
            return True

        min_open_left: int = 0
        max_open_left: int = 0

        for c in s:
            if c == '(':
                min_open_left += 1
                max_open_left += 1
            elif c == '*':
                min_open_left = max(min_open_left - 1, 0)
                max_open_left += 1
            elif c == ')':
                min_open_left = max(min_open_left - 1, 0)
                max_open_left -= 1
            else:
                return False

            if max_open_left < 0:
                return False

        return min_open_left == 0
