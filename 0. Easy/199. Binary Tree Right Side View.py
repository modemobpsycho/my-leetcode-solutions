# Definition for a binary tree node.
from typing import Any, List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None) -> None:
        self.val: int = val
        self.left: Any = left
        self.right: Any = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return root
        q: list[TreeNode] = [root]
        ans: list = []
        while q:
            t: list[TreeNode] = q.copy()
            q.clear()

            r = 0
            for node in t:
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                r = node.val
            ans.append(r)
        return ans
