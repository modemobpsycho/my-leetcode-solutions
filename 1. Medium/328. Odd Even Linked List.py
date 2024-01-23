# Definition for singly-linked list.
from typing import Any


class ListNode:
    def __init__(self, val=0, next=None) -> None:
        self.val: int = val
        self.next: Any | None = next


class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if head is None:
            return head
        odd, even = head, head.next
        even_head: Any | None = even
        while even and even.next:
            odd.next = even.next
            odd: Any = odd.next
            even.next = odd.next
            even: Any = even.next
        odd.next = even_head
        return head
