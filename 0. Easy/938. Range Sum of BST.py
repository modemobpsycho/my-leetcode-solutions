# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None) -> None:
        self.val: int = val
        self.left = left
        self.right = right


class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if not root:
            return 0

        left, right = 0, 0

        if root.val < high:
            right: int = self.rangeSumBST(root.right, low, high)
        if root.val > low:
            left: int = self.rangeSumBST(root.left, low, high)

        cur: int = root.val if low <= root.val <= high else 0

        return left + right + cur
