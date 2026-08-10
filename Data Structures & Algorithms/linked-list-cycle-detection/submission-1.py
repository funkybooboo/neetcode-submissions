class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        if head.next is head:
            return True

        nodes = set()

        current = head
        while current:
            if current in nodes:
                return True
            nodes.add(current)
            current = current.next

        return False