from typing import Optional


class Node:
    def __init__(self, x: int, next: "Node" = None, random: "Node" = None) -> None:
        self.val = int(x)
        self.next: Node = next
        self.random: Node = random


class Solution:
    def copyRandomList(self, head: "Optional[Node]") -> "Optional[Node]":
        if not head:
            return None

        temp: Node = head
        while temp:
            node = Node(temp.val)
            node.next = temp.next
            temp.next = node
            temp = node.next

        temp = head
        while temp:
            if not temp.random:
                temp.next.random = None
            else:
                temp.next.random = temp.random.next
            temp = temp.next.next

        temp = head.next
        while temp.next:
            temp.next = temp.next.next
            temp = temp.next

        return head.next
