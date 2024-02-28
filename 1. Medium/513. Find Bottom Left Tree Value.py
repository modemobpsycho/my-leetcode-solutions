from collections import deque
from typing import Any


class TreeNode:
    def __init__(self, val=0, left=None, right=None) -> None:
        self.val: int = val
        self.left: Any = left
        self.right: Any = right


class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        queue = deque([root])
        leftmost_val: int = root.val

        while queue:
            level_size: int = len(queue)

            for i in range(level_size):
                node: TreeNode = queue.popleft()

                if i == 0:
                    leftmost_val = node.val

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return leftmost_val
