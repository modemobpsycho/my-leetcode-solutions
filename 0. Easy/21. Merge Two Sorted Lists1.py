# Definition for singly-linked list.

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None) -> None:
        self.val: int = val
        self.next = next


class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        dummy = ListNode(None)
        prev: ListNode = dummy

        while list1 and list2:
            if list1.val > list2.val:
                prev.next = list2
                list2 = list2.next
            else:
                prev.next = list1
                list1 = list1.next

            prev = prev.next

        if list1:
            prev.next = list1
        if list2:
            prev.next = list2

        return dummy.next
