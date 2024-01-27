from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right: int = max(piles)
        while left < right:
            mid: int = (left + right) // 2

            hours_needed: int = sum((pile + mid - 1) // mid for pile in piles)

            if hours_needed <= h:
                right = mid
            else:
                left: int = mid + 1
        return left
