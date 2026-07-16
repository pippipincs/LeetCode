# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if not head or head.next == None:
            return head
        before = ListNode()
        after = ListNode()
        ptr = head
        ptr1 = before
        ptr2 = after
        while ptr:
            if ptr.val < x:
                ptr1.next = ptr
                ptr1 = ptr1.next
            else:
                ptr2.next = ptr
                ptr2 = ptr2.next
            ptr = ptr.next
        ptr1.next = None
        ptr2.next = None
        ptr1.next = after.next
        return before.next