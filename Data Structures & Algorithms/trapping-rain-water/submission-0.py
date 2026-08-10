class Solution:
    def trap(self, heights: List[int]) -> int:
        if not heights or len(heights) < 3:
            return 0
        n = len(heights)
        t = 0

        for i in range(n):
            l_m = r_m = heights[i]

            for j in range(i):
                l_m = max(l_m, heights[j])
            for j in range(i + 1, n):
                r_m = max(r_m, heights[j])

            t += min(l_m, r_m) - heights[i]
        return t
