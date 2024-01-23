# Definition for a binary tree node.
from typing import Any, List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None) -> None:
        self.val: int = val
        self.left: Any = left
        self.right: Any = right


class Solution:
    def post_orderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans: list = []

        def helper(node) -> None:
            if node:
                helper(node.left)
                helper(node.right)
                ans.append(node.val)

        helper(root)

        return ans
