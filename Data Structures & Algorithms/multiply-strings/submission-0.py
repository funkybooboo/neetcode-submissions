class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"

        len1, len2 = len(num1), len(num2)
        result = [0] * (len1 + len2)

        # Multiply each digit and store the result in the appropriate position
        for i in range(len1 - 1, -1, -1):
            for j in range(len2 - 1, -1, -1):
                mul = (ord(num1[i]) - ord('0')) * (ord(num2[j]) - ord('0'))
                p1, p2 = i + j, i + j + 1
                total = mul + result[p2]
                result[p1] += total // 10
                result[p2] = total % 10

        # Convert the result list to a string
        while len(result) > 1 and result[0] == 0:
            result.pop(0)  # Remove leading zeros

        return ''.join(map(str, result))
