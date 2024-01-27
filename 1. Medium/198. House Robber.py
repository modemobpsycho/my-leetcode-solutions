from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        a, b = 0, 0
        for n in nums:
            tmp: int = max(a + n, b)
            a: int = b
            b: int = tmp
        return b
