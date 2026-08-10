from typing import List


class Solution:
    def minOperations(self, logs: List[str]) -> int:
        count: int = 0

        for log in logs:
            if log == "../":
                if count > 0:
                    count -= 1
            elif log == "./":
                pass
            else:
                count += 1

        return count
