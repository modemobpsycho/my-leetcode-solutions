# Definition for singly-linked list.
from typing import Any, Optional


class ListNode:
    def __init__(self, val=0, next=None) -> None:
        self.val: int = val
        self.next: Any | None = next


class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        fast, slow, stack, max_twin_sum = head, head, [], 0

        while fast and fast.next:
            fast = fast.next.next
            stack.append(slow)
            slow = slow.next

        while slow:
            max_twin_sum: int = max(max_twin_sum, stack.pop().val + slow.val)
            slow = slow.next

        return max_twin_sum
