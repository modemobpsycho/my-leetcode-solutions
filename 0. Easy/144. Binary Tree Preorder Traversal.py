# Definition for a binary tree node.
from typing import Any, List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None) -> None:
        self.val: int = val
        self.left: Any | None = left
        self.right: Any | None = right


class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        return (
            [root.val]
            + self.preorderTraversal(root.left)
            + self.preorderTraversal(root.right)
            if root
            else []
        )
