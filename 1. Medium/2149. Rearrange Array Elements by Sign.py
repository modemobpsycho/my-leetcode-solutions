from typing import List


class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos: list[int] = [num for num in nums if num > 0]
        neg: list[int] = [num for num in nums if num < 0]

        res: list = []
        for p, n in zip(pos, neg):
            res.extend([p, n])

        return res
