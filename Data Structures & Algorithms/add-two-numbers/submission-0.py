class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        current = dummy

        c = 0
        while l1 or l2 or c:
            a = l1.val if l1 else 0
            b = l2.val if l2 else 0

            r = a + b + c
            c = r // 10
            r = r % 10

            current.next = ListNode(r)

            current = current.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return dummy.next
