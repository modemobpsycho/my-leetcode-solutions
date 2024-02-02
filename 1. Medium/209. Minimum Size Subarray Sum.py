from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if sum(nums) < target:
            return 0

        ans, s, l = len(nums), 0, 0

        for r, val in enumerate(nums):
            s += val

            while s >= target:
                s -= nums[l]
                ans: int = min(ans, r - l + 1)
                l += 1

        return ans
