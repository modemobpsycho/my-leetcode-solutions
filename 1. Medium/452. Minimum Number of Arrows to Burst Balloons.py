from typing import List


class Solution:
    def findMinArrowShots(self, p: List[List[int]]) -> int:
        lp: int = p[0][1]
        cnt = 0
        for i in sorted(p):
            if i[0] > lp:
                cnt += 1
                lp = i[1]
            lp = min(i[1], lp)
        return cnt + 1
