from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        n: int = len(gas)
        diff: list[int] = [gas[i] - cost[i] for i in range(n)]
        total = 0
        res = 0
        for i in range(n):
            total += diff[i]
            if total < 0:
                res: int = i + 1
                total = 0
        return res
