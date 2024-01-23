# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        l, r: int = 1, n

        while l <= r:
            mid: int = (l + r) // 2

            if isBadVersion(mid):
                r: int = mid - 1
            else:
                l: int = mid + 1

        return l
