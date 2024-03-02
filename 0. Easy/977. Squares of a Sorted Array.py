from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        slist: list = []
        for i in range(len(nums)):
            slist.append(nums[i] * nums[i])
        slist.sort()
        return slist
