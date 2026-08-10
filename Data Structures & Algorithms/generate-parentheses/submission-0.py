class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        res = []

        def backtrack(o_n: int, c_n: int):
            if o_n == c_n == n:
                res.append("".join(stack))
                return

            if o_n < n:
                stack.append("(")
                backtrack(o_n + 1, c_n)
                stack.pop()
            if c_n < o_n:
                stack.append(")")
                backtrack(o_n, c_n + 1)
                stack.pop()

        backtrack(0, 0)
        return res
