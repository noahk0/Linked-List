def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
    if k == 1:
        return head

    switch, node = True, ListNode(next = head)

    while node.next:
        cur = node

        for _ in range(k):
            cur = cur.next

            if not cur:
                return head

        pre = node.next
        cur = pre.next
            
        for _ in range(1, k):
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt

        node.next.next = nxt
        tmp = node.next
        node.next = pre
        node = tmp

        if switch:
            head, switch = pre, False

    return head
