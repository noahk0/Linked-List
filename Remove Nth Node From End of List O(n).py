def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
    remove = res = ListNode(next = head)

    for _ in range(n):
        head = head.next

    while head:
        head, remove = head.next, remove.next

    remove.next = remove.next.next

    return res.next
