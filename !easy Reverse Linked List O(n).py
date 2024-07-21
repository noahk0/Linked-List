def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    prev = None

    while head:
        cur = head.next
        head.next = prev
        prev = head
        head = cur

    return prev
