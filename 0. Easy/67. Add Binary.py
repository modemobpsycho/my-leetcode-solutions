from typing import Literal


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        len_a, len_b = len(a), len(b)
        if len_a > len_b:
            b = "0" * (len_a - len_b) + b
        else:
            a = "0" * (len_b - len_a) + a

        car = 0
        ans: Literal[''] = ""

        for i in range(len(a) - 1, -1, -1):
            d1 = int(a[i])
            d2 = int(b[i])

            car, d = divmod(d1 + d2 + car, 2)

            ans += str(d)

        if car:
            ans += str(car)

        return ans[::-1]
