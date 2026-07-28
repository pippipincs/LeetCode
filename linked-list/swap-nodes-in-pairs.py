# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        prev = dummy
        first = dummy.next 
        if first:
            second = first.next
        else:
            second = None
        while first and second:
            next_start = second.next
            prev.next = second
            second.next = first
            first.next = next_start
            prev = first
            first = next_start
            if first:
                second = first.next
            else:
                second = None
        return dummy.next
        
        