from typing import List


class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        l = []
        p = []
        for i in range(1, 10):
            s = str(i)
            for j in range(i + 1, 10):
                s += str(j)
                l.append(int(s))
        l.sort()
        for i in l:
            if i >= low and i <= high:
                p.append(i)
        return p
