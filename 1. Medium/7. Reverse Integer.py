from typing import Literal


class Solution:
    def reverse(self, x: int) -> int:
        max_int = pow(2, 31) - 1

        flag: Literal[-1, 1] = -1 if x < 0 else 1
        ans = 0
        x = abs(x)

        while x > 0:
            digit: int = x % 10
            if ans > max_int / 10:
                return 0
            ans: int = (ans * 10) + digit
            x //= 10

        return ans * flag
