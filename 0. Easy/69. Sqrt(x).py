class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        first, last: int = 1, x
        while first <= last:
            mid: int = first + (last - first) // 2
            if mid == x // mid:
                return mid
            elif mid > x // mid:
                last: int = mid - 1
            else:
                first: int = mid + 1
        return last
