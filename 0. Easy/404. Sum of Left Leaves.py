# Definition for a binary tree node.
from typing import Any, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None) -> None:
        self.val: int = val
        self.left: Any = left
        self.right: Any = right


class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        ans = 0
        stack: list[tuple[TreeNode]] = [(root, None)]

        while stack:
            cur, is_left = stack.pop()
            if not cur.left and not cur.right and is_left:
                ans += cur.val

            if cur.left:
                stack.append((cur.left, 1))
            if cur.right:
                stack.append((cur.right, 0))

        return ans
