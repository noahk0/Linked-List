def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
    node, copied = head, {None: None}

    while node:
        copied[node] = Node(node.val)
        node = node.next

    node = head

    while node:
        copied[node].next = copied[node.next]
        copied[node].random = copied[node.random]
        node = node.next

    return copied[head]
