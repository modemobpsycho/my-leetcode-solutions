from heapq import heappop, heappush
from typing import List


class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        res = s = 0

        pq = []

        for a, b in sorted(list(zip(nums1, nums2)), key=lambda ab: -ab[1]):
            s += a
            heappush(pq, a)

            if len(pq) > k:
                s -= heappop(pq)

            if len(pq) == k:
                res = max(res, s * b)

        return res
