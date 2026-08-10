class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result: List[int] = []
        for i in range(len(temperatures)):
            for j in range(i + 1, len(temperatures)):
                if temperatures[i] < temperatures[j]:
                    result.append(j - i)
                    break
            else:
                result.append(0)
        return result

