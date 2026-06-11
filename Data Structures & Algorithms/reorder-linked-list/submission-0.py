# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        l1=slow=fast=head

        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next

        l2=slow.next
        slow.next=None
        
        prev=None
        while l2 is not None:
            nxt=l2.next
            l2.next=prev
            prev=l2
            l2=nxt

        while prev:
            nxt1, nxt2 =l1.next, prev.next
            l1.next=prev
            prev.next=nxt1
            l1=nxt1
            prev=nxt2



        

        
                