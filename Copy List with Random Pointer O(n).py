def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
    node, copied = head, {None: None}

    while node:
        copied[node], node = Node(node.val), node.next

    node = head

    while node:
        copied[node].next, copied[node].random, node = copied[node.next], copied[node.random], node.next

    return copied[head]
