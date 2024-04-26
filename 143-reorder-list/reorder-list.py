# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        # Find middle of list
        slow, fast = head, head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # reverse from middle to end of list -> curr is head of middle
        curr = slow.next
        prev = slow.next = None

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        
        # prev is head of reversed list
        # Merge lists prev & head
        curr = head
        while prev and curr:
            p, q = curr.next, prev.next
            curr.next = prev
            prev.next = p
            curr , prev = p, q
        
        return head
        

