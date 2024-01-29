import heapq
from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        cit: list[int] = [-i for i in citations]
        heapq.heapify(cit)
        res = 0
        i = 1
        
        while i <= len(citations):
            val: int = heapq.heappop(cit)
            if -val < i:
                break
            else:
                res: int = i
            i += 1

        return res
