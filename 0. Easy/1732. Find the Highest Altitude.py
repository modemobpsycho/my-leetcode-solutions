from typing import List


class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        ans = 0
        cont = 0
        for i in gain:
            cont += i
            ans: int = max(cont, ans)
        return ans
