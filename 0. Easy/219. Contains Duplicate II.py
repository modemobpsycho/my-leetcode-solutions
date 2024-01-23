from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        d: dict = {}

        for i, num in enumerate(nums):
            if num in d and i - d[num] <= k:
                return True
            d[num] = i

        return False
