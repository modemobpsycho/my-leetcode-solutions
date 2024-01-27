from typing import List


class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        even: list = []
        odd: list = []
        for val in nums:
            if val % 2 == 0:
                even += [val]
            else:
                odd += [val]

        return even + odd
