from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1

        while left < right:
            mid: int = (left + right) // 2
            if nums[mid] > nums[mid + 1]:
                right: int = mid
            else:
                left: int = mid + 1

        return left
