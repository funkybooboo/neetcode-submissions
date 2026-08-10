from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        # Base case: empty list
        if not head:
            return None

        # Recursively process the rest of the list
        head.next = self.removeElements(head.next, val)

        # If current node should be removed, return the next node
        # Otherwise, return the current node
        return head.next if head.val == val else head
