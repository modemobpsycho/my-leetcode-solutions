# Definition for a binary tree node.
from typing import Any, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None) -> None:
        self.val: int = val
        self.left: Any = left
        self.right: Any = right


class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        left: int = self.minDepth(root.left)
        right: int = self.minDepth(root.right)

        if left != 0 and right != 0:
            return 1 + min(left, right)
        return 1 + left + right
