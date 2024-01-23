# Definition for a binary tree node.
from typing import Deque, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        q = Deque([root])
        out, max_level = 1, root.val
        i = 1
        while q:
            level_sum = 0
            size = len(q)
            for _ in range(size):
                e = q.popleft()
                level_sum += e.val
                if e.left:
                    q.append(e.left)
                if e.right:
                    q.append(e.right)
            if level_sum > max_level:
                out, max_level = i, level_sum
            i += 1
        return out
