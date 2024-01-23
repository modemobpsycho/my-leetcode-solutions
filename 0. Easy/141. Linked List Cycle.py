# Definition for singly-linked list.
from typing import Any, Optional


class ListNode:
    def __init__(self, x) -> None:
        self.val: Any = x
        self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        seen = set()
        while head:
            if head in seen:
                return True
            seen.add(head)
            head = head.next
        return False
