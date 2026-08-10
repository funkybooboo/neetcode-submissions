class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        current = head
        count = 0

        # First, check if there are at least k nodes remaining to reverse
        while current and count < k:
            current = current.next
            count += 1

        # If we have at least k nodes, proceed with reversal
        if count == k:
            # Recursively reverse the next part of the list
            reversed_head = self.reverseKGroup(current, k)

            # Reverse current k-group
            while count > 0:
                temp = head.next       # store next node
                head.next = reversed_head  # point current node to the reversed part
                reversed_head = head   # update the new head of reversed section
                head = temp            # move to the next node in the original list
                count -= 1

            # After reversal, 'reversed_head' is the new head of this section
            return reversed_head

        # If there are fewer than k nodes, leave them as-is
        return head
