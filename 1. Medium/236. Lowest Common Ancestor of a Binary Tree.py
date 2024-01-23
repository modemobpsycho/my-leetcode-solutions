# Definition for a binary tree node.
from typing import Any


class TreeNode:
    def __init__(self, x) -> None:
        self.val: Any = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":
        if root == None:
            return None
        if root == p or root == q:
            return root
        leftNode: TreeNode = self.lowestCommonAncestor(root.left, p, q)
        rightNode: TreeNode = self.lowestCommonAncestor(root.right, p, q)
        if leftNode and rightNode:
            return root
        if leftNode != None:
            return leftNode
        else:
            return rightNode
