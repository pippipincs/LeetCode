# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None
        if not head.next:
            return head

        tail = head
        n = 1
        while tail.next:
            tail = tail.next
            n += 1
        tail.next = head

        v = n - k % n - 1
        tail = head
        while v > 0:
            tail = tail.next
            v -= 1
        head = tail.next
        tail.next = None
        return head
