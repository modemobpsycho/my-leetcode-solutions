# Definition for a binary tree node.
from typing import Literal, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None) -> None:
        self.val: int = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def helper(
            root,
        ) -> (
            tuple[Literal[True], Literal[0]]
            | tuple[Literal[False], Literal[-1]]
            | tuple
        ):
            if not root:
                return True, 0

            lb, lh = helper(root.left)
            rb, rh = helper(root.right)

            if not lb or not rb:
                return False, -1

            return abs(lh - rh) < 2, 1 + max(lh, rh)

        return helper(root)[0]
