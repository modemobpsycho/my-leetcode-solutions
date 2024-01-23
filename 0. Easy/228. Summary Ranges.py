from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []

        s: int = nums[0]
        nums.append(float("inf"))
        ans: list = []
        for i in range(1, len(nums)):
            if nums[i] - nums[i - 1] > 1:
                end: int = nums[i - 1]
                if s == end:
                    ans.append(str(s))
                else:
                    ans.append(f"{s}->{end}")

                s = nums[i]

        return ans
