from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        dp: list[int] = [0] * (len(nums) + 1)

        for i in range(len(nums)):
            if nums[i]:
                dp[i + 1] = dp[i] + 1
            else:
                dp[i + 1] = 0

        return max(dp)
