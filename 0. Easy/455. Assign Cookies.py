from typing import List


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()

        i = 0
        for coo in s:
            if coo >= g[i]:
                i += 1
            if i == len(g):
                break
        return i
