def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
    res = ListNode(next = head)

    for _ in range(n):
        head = head.next

    remove = res

    while head:
        head, remove = head.next, remove.next

    remove.next = remove.next.next

    return res.next
