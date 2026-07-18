# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def hasKNodes(node, k):
            count = 0
            while node and count < k:
                node = node.next
                count += 1
            return count == k

        dummy = ListNode(0, head)
        groupPrev = dummy

        while True:
            if not hasKNodes(groupPrev.next, k):
                break

            # Reverse k nodes starting at groupPrev.next
            prev, curr = None, groupPrev.next
            groupTail = curr  # this node will become the tail of this reversed group
            for _ in range(k):
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt

            # prev is now the new head of this reversed group
            # groupTail is now the tail of this reversed group, connect it to what's next
            temp = groupPrev.next  # old head of group, still points nowhere useful now
            groupPrev.next = prev
            groupTail.next = curr

            # Move groupPrev to the tail of the just-reversed group for the next iteration
            groupPrev = groupTail

        return dummy.next