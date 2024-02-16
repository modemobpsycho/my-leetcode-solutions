import collections as col
from typing import List


class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        counter = col.Counter(arr)
        uniques: int = len(counter)
        for count in sorted(counter.values()):
            k -= count
            if k < 0:
                break
            uniques -= 1
        return uniques
