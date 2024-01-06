class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        new = 0
        original = x

        while x:
            x, d = divmod(x, 10)
            new = new * 10 + d

        return new == original


class Solution1(object):
    def isPalindrome(self, x):
        return str(x) == str(x)[::-1]
