class DoubleNode:
    def __init__(self, key, val, prev, nextnode):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = nextnode
class LRUCache:

    def __init__(self, capacity: int):
        self.dict = {}
        self.capacity = capacity
        self.count = 0
        self.head = DoubleNode(0, 0, None, None)
        self.tail = self.head
    def get(self, key: int) -> int:
        if key in self.dict:
            node = self.dict[key]
            self.remove(node)
            self.insert(node)
            return node.val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.dict:
            node = self.dict[key]
            node.val = value
            self.remove(node)
            self.insert(node)
        else:
            node = DoubleNode(key, value, None, None)
            self.dict[key] = node
            if self.count >= self.capacity:
                node_delete = self.head.next
                self.remove(node_delete)
                del self.dict[node_delete.key]
            else:
                self.count += 1
            self.insert(node)
    def remove(self, node):
        if self.tail == node:
            self.tail = self.tail.prev
            self.tail.next = None
        else:
            node.prev.next = node.next
            node.next.prev = node.prev
    def insert(self, node):
        self.tail.next = node
        node.prev = self.tail
        self.tail = self.tail.next

                



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)