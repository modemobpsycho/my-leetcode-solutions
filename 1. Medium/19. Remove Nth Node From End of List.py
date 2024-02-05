from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None) -> None:
        self.val: int = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        first: ListNode | None = head
        second: ListNode | None = head

        for i in range(n):
            first = first.next

        if not first:
            return head.next

        while first.next:
            second = second.next
            first = first.next

        second.next = second.next.next

        return head
