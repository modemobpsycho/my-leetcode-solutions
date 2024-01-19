from typing import List


class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        length = len(candies)
        maximum = max(candies)
        ans = []
        for i in range(length):
            sumValue = candies[i] + extraCandies
            if sumValue >= maximum:
                ans.append(True)
            else:
                ans.append(False)

        return ans
