from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        s, ans = sum(nums), 0
        for i in range(len(nums)):
            ans += nums[i]
            if ans == s:
                return i
            s -= nums[i]
        return -1
