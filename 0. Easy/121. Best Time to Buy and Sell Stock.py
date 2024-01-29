from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        l = 0
        for r in range(len(prices)):
            if prices[l] > prices[r]:
                l: int = r
            else:
                profit: int = max(profit, prices[r] - prices[l])
        return profit
