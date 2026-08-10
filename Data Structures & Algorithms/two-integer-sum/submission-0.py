class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        m: Dict[int, int] = {}
        for i, n in enumerate(nums):
            c: int = target - n
            if c in m:
                return [m[c], i]
            m[n] = i
        return []
