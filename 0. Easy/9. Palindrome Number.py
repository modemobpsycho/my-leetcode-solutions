class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        new = 0
        original: int = x

        while x:
            x, d: int = divmod(x, 10)
            new: int = new * 10 + d

        return new == original


class Solution1(object):
    def isPalindrome(self, x) -> bool:
        return str(x) == str(x)[::-1]
