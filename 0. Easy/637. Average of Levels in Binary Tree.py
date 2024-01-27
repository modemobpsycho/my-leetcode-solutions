# Definition for a binary tree node.
from collections import deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None) -> None:
        self.val: int = val
        self.left = left
        self.right = right


class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        ans = []
        q = deque([root])

        while q:
            c_sum = 0
            cnt = 0

            for _ in range(len(q)):
                cur: TreeNode | None = q.popleft()
                c_sum += cur.val
                cnt += 1

                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)

            ans.append(c_sum / cnt)

        return ans
