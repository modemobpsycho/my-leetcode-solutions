from typing import List


class Solution:
    def jump(self: int, nums: List[int]) -> int:
        start, end, count = 0, 0, 0
        for i in range(len(nums) - 1):
            start: int = max(start, i + nums[i])
            if end == i:
                end: int = start
                count += 1
        return count
