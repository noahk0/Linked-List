def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    prev = None

    while head:
        cur = head.next
        head.next, prev, head = prev, head, cur

    return prev
