from collections import Counter
from typing import List


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        return max(Counter(Counter(arr).values()).values()) < 2
