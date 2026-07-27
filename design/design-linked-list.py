class DoubleNode:
    def __init__(self, val = 0, prev = None, next = None):
        self.val = val
        self.prev = prev
        self.next = next
class MyLinkedList:

    def __init__(self):
        self.head = DoubleNode()
        self.tail = DoubleNode()
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, index: int) -> int:
        ptr = self.head
        while index >= 0 and ptr:
            ptr = ptr.next
            index -= 1
        if ptr != self.head and ptr != self.tail and ptr:

            return ptr.val
        else:
            return -1

    def addAtHead(self, val: int) -> None:
        node = DoubleNode(val)
        first = self.head.next
        self.head.next = node
        node.next = first
        first.prev = node
        node.prev = self.head

    def addAtTail(self, val: int) -> None:
        node = DoubleNode(val)
        last = self.tail.prev
        last.next = node
        node.next = self.tail
        self.tail.prev = node
        node.prev = last

    def addAtIndex(self, index: int, val: int) -> None:
        ptr = self.head
        node = DoubleNode(val)
        while index >= 0:
            ptr = ptr.next
            index -= 1
        if ptr and ptr != self.head:
            prev_node = ptr.prev
            prev_node.next = node
            node.next = ptr
            ptr.prev = node
            node.prev = prev_node
        else:
            return 

    def deleteAtIndex(self, index: int) -> None:
        ptr = self.head
        while index >= 0:
            ptr = ptr.next
            index -= 1
        if ptr and ptr != self.tail and ptr != self.head:
            prev_ = ptr.prev
            next_ = ptr.next
            prev_.next = next_
            next_.prev = prev_


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)