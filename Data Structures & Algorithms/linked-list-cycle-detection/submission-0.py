# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        curr=head
        hashSet=set()
        while curr is not None:
            if curr not in hashSet:
                hashSet.add(curr)
            else:
                return True
            curr=curr.next
        
        return False