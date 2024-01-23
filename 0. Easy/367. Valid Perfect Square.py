class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num == 1:
            return True

        l, r = 1, num // 2

        while l <= r:
            mid: int = (l + r) // 2
            square: int = mid * mid

            if square == num:
                return True

            if square < num:
                l: int = mid + 1
            else:
                r: int = mid - 1

        return False
