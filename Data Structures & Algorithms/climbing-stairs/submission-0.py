class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n

        memo = [-1] * (n + 1)

        def count_ways(current_step: int) -> int:
            if current_step > n:
                return 0
            if current_step == n:
                return 1
            if memo[current_step] != -1:
                return memo[current_step]

            one_step = count_ways(current_step + 1)
            two_steps = count_ways(current_step + 2)

            memo[current_step] = one_step + two_steps
            return memo[current_step]

        return count_ways(0)
