from typing import List


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        count: dict = {}
        start = 0
        for end, Right in enumerate(nums):
            count[Right] = 1 + count.get(Right, 0)
            if 0 not in count:
                count[0] = 0
            if count[0] > k:
                count[nums[start]] -= 1
                start += 1
        return end - start + 1
