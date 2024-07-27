def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    head = num = ListNode()

    while l1 or l2:
        add = num.val
            
        add += l1.val if l1 else 0
        add += l2.val if l2 else 0

        num.val, num.next = add % 10, ListNode(add // 10) if add // 10 or l1 and l1.next or l2 and l2.next else None
        num, l1, l2 = num.next, l1.next if l1 else None, l2.next if l2 else None

    return head
