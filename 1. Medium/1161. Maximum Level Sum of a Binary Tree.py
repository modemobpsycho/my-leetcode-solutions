# Definition for a binary tree node.
from typing import Any, Deque, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None) -> None:
        self.val: int = val
        self.left: Any | None = left
        self.right: Any | None = right


class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        q = Deque([root])
        out, max_level: int = 1, root.val
        i = 1
        while q:
            level_sum = 0
            size: int = len(q)
            for _ in range(size):
                e: TreeNode | None = q.popleft()
                level_sum += e.val
                if e.left:
                    q.append(e.left)
                if e.right:
                    q.append(e.right)
            if level_sum > max_level:
                out, max_level = i, level_sum
            i += 1
        return out
