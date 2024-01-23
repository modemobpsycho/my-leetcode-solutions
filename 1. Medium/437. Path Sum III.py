from typing import Any, Literal, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None) -> None:
        self.val: int = val
        self.left: Any | None = left
        self.right: Any | None = right


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        def dfs(node, target) -> Any | Literal[0]:
            if not node:
                return 0
            count = 0
            if node.val == target:
                count += 1
            count += dfs(node.left, target - node.val)
            count += dfs(node.right, target - node.val)
            return count

        if not root:
            return 0
        return (
            dfs(root, targetSum)
            + self.pathSum(root.left, targetSum)
            + self.pathSum(root.right, targetSum)
        )
