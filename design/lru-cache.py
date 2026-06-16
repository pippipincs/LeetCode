class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None
    
class LRUCache:

    def __init__(self, capacity: int):
        self.mapping = {}
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self.mapping:
            return -1
        else:
            node = self.mapping[key]
            self.remove(node)
            self.add(node)
            return node.value


    def put(self, key: int, value: int) -> None:
        if key in self.mapping:
            node = self.mapping[key]
            self.remove(node)
            node.value = value
            self.mapping[key] = node
            self.add(node)
        else:
            node = Node(key, value)
            self.add(node)
            self.mapping[key] = node
            if len(self.mapping) > self.capacity:
                first = self.head.next
                k = first.key
                self.remove(first)
                del self.mapping[k]



    def remove(self, node):
        prevnode = node.prev
        nextnode = node.next
        prevnode.next = nextnode
        nextnode.prev = prevnode
        node.prev = None
        node.next = None 
    def add(self, node):
        prevnode = self.tail.prev
        prevnode.next = node
        node.prev = prevnode
        node.next = self.tail
        self.tail.prev = node


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)