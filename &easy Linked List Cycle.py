def hasCycle(self, head: Optional[ListNode]) -> bool:
    fast = head

    while fast and fast.next:
        head, fast = head.next, fast.next.next

        if head == fast:
            return True

    return False
