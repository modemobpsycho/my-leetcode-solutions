# Definition for a binary tree node.
from typing import Any, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None) -> None:
        self.val: int = val
        self.left: Any | None = left
        self.right: Any | None = right


class Solution:
    def recursive(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p and q:
            return (
                p.val == q.val
                and self.recursive(p.left, q.right)
                and self.recursive(p.right, q.left)
            )
        else:
            return p == q

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        p: Any | None = root.left
        q: Any | None = root.right
        return self.recursive(p, q)
