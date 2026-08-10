import heapq

class MedianFinder:

    def __init__(self):
        self.lowers: list[int] = []   # max-heap (as negative values)
        self.uppers: list[int] = []   # min-heap

    def addNum(self, num: int) -> None:
        if not self.lowers or num <= -self.lowers[0]:
            heapq.heappush(self.lowers, -num)
        else:
            heapq.heappush(self.uppers, num)

        # Balance heaps
        if len(self.lowers) > len(self.uppers) + 1:
            heapq.heappush(self.uppers, -heapq.heappop(self.lowers))
        elif len(self.uppers) > len(self.lowers):
            heapq.heappush(self.lowers, -heapq.heappop(self.uppers))

    def findMedian(self) -> float:
        total = len(self.lowers) + len(self.uppers)
        if total % 2 == 0:
            return (-self.lowers[0] + self.uppers[0]) / 2
        else:
            return -self.lowers[0]
