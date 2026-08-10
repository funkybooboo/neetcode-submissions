class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for t in tokens:
            if t == "+":
                stack[-2] += stack[-1]  # Directly update the second-to-last element
                stack.pop()  # Pop the last element
            elif t == "-":
                stack[-2] -= stack[-1]  # Directly update the second-to-last element
                stack.pop()  # Pop the last element
            elif t == "*":
                stack[-2] *= stack[-1]  # Directly update the second-to-last element
                stack.pop()  # Pop the last element
            elif t == "/":
                a, b = stack[-2], stack[-1]
                stack.pop()  # Pop the last element
                stack[-1] = int(a / b)  # Update the second-to-last element with the result
            else:
                stack.append(int(t))  # Convert token to integer and append
        return stack[0]  # Only one item should be left on the stack

