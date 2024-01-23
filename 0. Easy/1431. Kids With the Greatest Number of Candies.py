from typing import List


class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        length: int = len(candies)
        maximum: int = max(candies)
        ans: list = []
        for i in range(length):
            sumValue: int = candies[i] + extraCandies
            if sumValue >= maximum:
                ans.append(True)
            else:
                ans.append(False)

        return ans
