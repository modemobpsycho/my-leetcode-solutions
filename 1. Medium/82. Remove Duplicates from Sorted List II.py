class ListNode:
    def __init__(self, val=0, next=None) -> None:
        self.val: int = val
        self.next: Any | None = next


from typing import Any, Optional


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head
        temp: ListNode = head
        dummy = pre = ListNode()
        while temp and temp.next:
            if temp.val == temp.next.val:
                while temp and temp.next and temp.val == temp.next.val:
                    temp = temp.next
                temp = temp.next
                pre.next = temp
            else:
                pre.next = temp
                pre: ListNode = pre.next
                temp = temp.next
        return dummy.next
