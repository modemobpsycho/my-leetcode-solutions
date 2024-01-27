# Definition for a binary tree node.
from typing import Any, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None) -> None:
        self.val: int = val
        self.left: Any | None = left
        self.right: Any | None = right


class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        seen = set()
        stack: list[TreeNode | None] = [root]

        while stack:
            cur: TreeNode | None = stack.pop()
            if k - cur.val in seen:
                return True
            seen.add(cur.val)
            if cur.left:
                stack.append(cur.left)
            if cur.right:
                stack.append(cur.right)

        return False
