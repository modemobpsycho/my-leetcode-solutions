from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            mid: int = (l + r) // 2

            if nums[mid] == target:
                return mid

            if nums[mid] > target:
                r: int = mid - 1
            else:
                l: int = mid + 1

        return -1
