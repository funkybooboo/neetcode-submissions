class Solution:
    def numDecodings(self, s: str) -> int:
        def is_int(value):
            try:
                int(value)
                return True
            except (ValueError, TypeError):
                return False

        if len(s) == 0 or not is_int(s) or s[0] == '0':
            return 0

        memo = {}

        def dfs(i: int) -> int:
            if i in memo:
                return memo[i]
            if i == len(s):
                return 1
            if s[i] == '0':
                return 0
            # Take one digit
            count = dfs(i + 1)
            # Take two digits
            if i + 1 < len(s) and 10 <= int(s[i:i + 2]) <= 26:
                count += dfs(i + 2)

            memo[i] = count

            return count

        return dfs(0)
