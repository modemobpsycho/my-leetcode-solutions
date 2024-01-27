from itertools import combinations
from typing import List


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        l: list[int] = [i for i in range(1, 10)]
        p = []
        c = combinations(l, k)
        for i in list(c):
            if sum(i) == n:
                p.append(list(i))
        return p
