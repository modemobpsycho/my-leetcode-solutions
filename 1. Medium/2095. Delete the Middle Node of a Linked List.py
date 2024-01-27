# Definition for singly-linked list.
from typing import Any, Optional


class ListNode:
    def __init__(self, val=0, next=None) -> None:
        self.val: int = val
        self.next: Any = next


class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        n = 0
        temp: ListNode | None = head
        while temp:
            n += 1
            temp = temp.next

        temp = head
        x: int = n // 2
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
