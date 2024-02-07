from typing import Any, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None) -> None:
        self.val: int = val
        self.left: Any = left
        self.right: Any = right


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False

        if not root.left and not root.right:
            return targetSum == root.val

        left_sum: bool = self.hasPathSum(root.left, targetSum - root.val)
        right_sum: bool = self.hasPathSum(root.right, targetSum - root.val)

        return left_sum or right_sum