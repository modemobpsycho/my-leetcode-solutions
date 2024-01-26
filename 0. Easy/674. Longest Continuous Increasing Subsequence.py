from typing import List


class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        dp: list[int] = [1] * len(nums)

        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                dp[i] = dp[i - 1] + 1
        return max(dp)
