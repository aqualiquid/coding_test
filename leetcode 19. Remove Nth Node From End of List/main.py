from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head.next is None:
            return None

        dummy = ListNode(0)
        dummy.next = head

        first = dummy
        second = dummy

        # move first pointer from head(i.e., start) to the Nth node
        for _ in range(n+1):
            first = first.next

        # move first and second pointer simultaneously
        while first is not None:
            first = first.next
            second = second.next
        # removing the n'th node
        second.next = second.next.next
        return dummy.next

