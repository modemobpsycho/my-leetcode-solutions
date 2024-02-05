from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None) -> None:
        self.val: int = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self) -> None:
        self.prev = None

    def flatten(self, root: Optional[TreeNode]) -> None:
        if not root:
            return
        self.flatten(root.right)
        self.flatten(root.left)
        root.right = self.prev
        root.left = None
        self.prev: TreeNode = root
