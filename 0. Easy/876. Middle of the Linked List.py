# Definition for singly-linked list.
from typing import Any, Optional


class ListNode:
    def __init__(self, val=0, next=None) -> None:
        self.val: int = val
        self.next: Any = next


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow: ListNode | None = head
        fast: ListNode | None = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow
