# Definition for singly-linked list.
from typing import Any, Optional


class ListNode:
    def __init__(self, val=0, next=None) -> None:
        self.val: int = val
        self.next: Any = next


class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode(None, next=head)

        cur: ListNode = head
        prev: ListNode = dummy

        while cur:
            if cur.val == val:
                prev.next = cur.next
            else:
                prev = cur

            cur = cur.next

        return dummy.next
