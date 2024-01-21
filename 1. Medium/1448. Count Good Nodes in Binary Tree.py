# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def goodNodes(self, root: TreeNode, path=float("-inf")) -> int:
        if not root:
            return 0
        else:
            if root.val >= path:
                return (
                    1
                    + self.goodNodes(root.left, root.val)
                    + self.goodNodes(root.right, root.val)
                )
            else:
                return self.goodNodes(root.left, path) + self.goodNodes(
                    root.right, path
                )
