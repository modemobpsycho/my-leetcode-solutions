
from collections import deque


class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None) -> None:
        self.val: int = val
        self.left: Node = left
        self.right: Node = right
        self.next: Node = next


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        q = deque([root])

        while q:
            n: int = len(q)
            prev = None

            for _ in range(n):
                node: Node = q.popleft()

                if node:
                    if prev:
                        prev.next = node
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)

                prev: Node = node

        return root
