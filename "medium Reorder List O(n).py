def reorderList(self, head: Optional[ListNode]) -> None:
    fast = slow = head

    while fast and fast.next:
        slow, fast = slow.next, fast.next.next

    pre = None
        
    while slow:
        cur = slow.next
        slow.next, pre, slow = pre, slow, cur

    while pre.next:
        tmp = head.next
        head.next, pre, head.next.next, head = pre, pre.next, tmp, tmp
