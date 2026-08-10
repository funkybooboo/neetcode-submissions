class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head:
            return

        # Step 1: Collect nodes in an array
        nodes = []
        current = head
        while current:
            nodes.append(current)
            current = current.next

        # Step 2: Reorder using two pointers
        left, right = 0, len(nodes) - 1
        while left < right:
            nodes[left].next = nodes[right]
            left += 1
            if left == right:
                break
            nodes[right].next = nodes[left]
            right -= 1

        # Step 3: Terminate the reordered list properly
        nodes[left].next = None
