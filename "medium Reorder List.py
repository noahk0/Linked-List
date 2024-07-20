def reorderList(self, head: Optional[ListNode]) -> None:
    fast = slow = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    pre = None
        
    while slow:
        cur = slow.next
        slow.next = pre
        pre = slow
        slow = cur

    while pre.next:
        tmp = head.next
        head.next = pre
        pre = pre.next
        head.next.next = tmp
        head = tmp
