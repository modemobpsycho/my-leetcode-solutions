# Definition for singly-linked list.
from typing import Any, Optional


class ListNode:
    def __init__(self, val=0, next=None) -> None:
        self.val: int = val
        self.next: Any = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        cur: ListNode = head

        while cur:
            cur.next, prev, cur = prev, cur, cur.next

        return prev
