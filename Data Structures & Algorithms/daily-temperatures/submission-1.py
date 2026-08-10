class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res: List[int] = [0] * len(temperatures)
        stack: List[Tuple[int, int]] = []  # pair: [index, temp]

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][1]:
                s_i, _  = stack.pop()
                res[s_i] = i - s_i
            stack.append((i, t))
        return res
