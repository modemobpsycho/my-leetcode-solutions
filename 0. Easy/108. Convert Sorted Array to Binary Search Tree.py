# Definition for a binary tree node.
from typing import Any, List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None) -> None:
        self.val: int = val
        self.left: Any = left
        self.right: Any = right


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def helper(l, r) -> TreeNode:
            if l <= r:
                mid = (l + r) // 2

                root = TreeNode(nums[mid])

                root.left = helper(l, mid - 1)
                root.right = helper(mid + 1, r)

                return root

        return helper(0, len(nums) - 1)
