class NodeWrapper:
    def __init__(self, node):
        self.node = node

    def __lt__(self, other):
        return self.node.val < other.node.val


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None

        dummy = ListNode()
        current = dummy
        minHeap = []

        for node in lists:
            if node:
                heapq.heappush(minHeap, NodeWrapper(node))

        while minHeap:
            nodeWrapper = heapq.heappop(minHeap)
            current.next = nodeWrapper.node
            current = current.next

            if nodeWrapper.node.next:
                heapq.heappush(minHeap, NodeWrapper(nodeWrapper.node.next))

        return dummy.next
