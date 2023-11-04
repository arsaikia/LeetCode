# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x 
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        prevHead = ListNode(0, head)

        l, r = prevHead, prevHead
        while r and r.next:
            
            l = l.next
            r = r.next.next

            if l == r:
                return True
        
        return
        