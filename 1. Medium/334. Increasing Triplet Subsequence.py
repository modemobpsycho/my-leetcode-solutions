from typing import List


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first = second = float("inf")
        for n in nums:
            if n <= first:
                first: int = n
            elif n <= second:
                second: int = n
            else:
                return True
        return False
