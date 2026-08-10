from typing import Optional


class ListNode:
    def __init__(self, val: int= 0, next: Optional['ListNode']=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False

        # get slow in the middle
        fast = head
        slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        # reverse second half
        middle = None
        while slow:
            temp = slow.next
            slow.next = middle
            middle = slow
            slow = temp

        # check palindrome
        left = head
        right = middle
        while right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next

        return True
