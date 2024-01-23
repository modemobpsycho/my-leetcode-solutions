# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:


from typing import Any


class Solution:
    def guessNumber(self, n: int) -> int:
        l, r = 1, n

        while l <= r:
            mid: int = (l + r) // 2

            check: Any = guess(mid)

            if check == 0:
                return mid

            if check < 0:
                r: int = mid - 1
            else:
                l: int = mid + 1
