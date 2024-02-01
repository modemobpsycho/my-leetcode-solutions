from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None) -> None:
        self.val: int = val
        self.next = next


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head == None or head.next == None or k == 0:
            return head
        length = 1
        curr: ListNode = head
        while curr.next:
            curr = curr.next
            length += 1
        curr.next = head
        k %= length
        rotate: int = length - k
        while rotate:
            curr = curr.next
            rotate -= 1
        head = curr.next
        curr.next = None
        return head
