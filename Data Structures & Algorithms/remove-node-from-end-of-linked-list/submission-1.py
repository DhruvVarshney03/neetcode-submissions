# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy=ListNode(0,head)

        
        # length=0
        # while curr:
        #     length+=1
        #     curr=curr.next

        # curr=dummy

        # target=length-n
        # for _ in range(target):
        #     curr=curr.next
        # curr.next=curr.next.next

        # return dummy.next
        
        slow=fast=dummy

        for _ in range(n+1):
            fast=fast.next

        while fast:
            slow=slow.next
            fast=fast.next

        slow.next=slow.next.next

        return dummy.next           

        