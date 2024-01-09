# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # if there is no head OR head is equal to 1 (considered as useless k)
        if head is None or k==1:
            return head

        dummy = ListNode(0)
        dummy.next = head   # b/c, dummy.next points out ListNode(1)
        prev, crnt, nxt = dummy, None, dummy

        # counting whole number of nodes
        count = 0
        while crnt:
            crnt = crnt.next
            count += 1

        # flipping part (divided into k'th element)
        while count >= k:
            # pre should not be modfied since it doesn't need to be altered at this moment
            crnt = prev.next
            nxt  = crnt.next
            # iterating from crnt to k+crnt in order to swap between prev and nxt
            for _ in range(1,k):
                crnt.next = nxt.next
                nxt.next  = prev.next
                prev.next  = nxt #(crnt)
                nxt       = crnt.next
            prev = crnt
            count -= k

        return dummy.next

    def printListNode(node):
        while node:
            print(node.val, end=" -> ")
            node = node.next
        print("None")










