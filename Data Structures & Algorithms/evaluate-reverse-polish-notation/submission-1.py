class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack: List[int] = []
        operators = {
            "+": lambda a, b: a + b,
            "-": lambda a, b: a - b,
            "*": lambda a, b: a * b,
            "/": lambda a, b: int(a / b)  # ensure truncation towards zero
        }

        for t in tokens:
            if t in operators:
                b = stack.pop()
                a = stack.pop()
                stack.append(operators[t](a, b))
            else:
                stack.append(int(t))

        return stack.pop()
