# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        n = 0
        temp = head
        cur = head
        while temp:
            n += 1
            temp = temp.next

        temp = head
        x = n // 2
        i = 0

        if x == 0:
            return None

        while temp:
            i += 1
            if i != x:
                temp = temp.next
            else:
                temp.next = temp.next.next
        return head
