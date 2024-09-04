def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    l = deque(lists)

    while 1 < len(l):
        l1, l2 = l.pop(), l.pop()
        cur = head = ListNode()

        while l1 and l2:
            if l1.val < l2.val:
                cur.next, l1 = l1, l1.next
            else:
                cur.next, l2 = l2, l2.next

            cur = cur.next

        cur.next = l1 or l2
        l.appendleft(head.next)

    return l.pop() if l else None
