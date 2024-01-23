class Solution:
    def addDigits(self, num: int) -> int:

        while num >= 10:

            cur: int = num

            new_num = 0

            while cur:

                cur, d: int = divmod(cur, 10)

                new_num += d

            num = new_num

        return num
