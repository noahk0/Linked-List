class Node:
    def __init__(self, key: int):
        self.key = key
        self.prev = self.next = None
    
class LRUCache:

    def __init__(self, capacity: int):
        self.cap, self.cache, self.new, self.old = capacity, {}, Node(0), Node(0)
        self.new.prev, self.old.next = self.old, self.new

    def pop(self, node: Node):
        node.prev.next, node.next.prev = node.next, node.prev

    def push(self, node: Node):
        node.next, node.prev = self.new, self.new.prev
        node.prev.next = self.new.prev = node

    def get(self, key: int) -> int:
        if key in self.cache:
            self.pop(self.cache[key][1])
            self.push(self.cache[key][1])

            return self.cache[key][0]

        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.pop(self.cache[key][1])

        self.cache[key] = (value, Node(key))
        self.push(self.cache[key][1])

        if self.cap < len(self.cache):
            del self.cache[self.old.next.key]
            self.pop(self.old.next)
