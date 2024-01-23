# Definition for a binary tree node.
from typing import Any, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None) -> None:
        self.val: int = val
        self.left: Any = left
        self.right: Any = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return (
            max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1 if root else 0
        )
