class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        m: Dict[int, int] = {}
        for n in nums:
            m[n] = m.get(n, 0) + 1

        s = sorted(m.items(), key=lambda x: x[1], reverse=True)

        return [i[0] for i in s[:k]]
