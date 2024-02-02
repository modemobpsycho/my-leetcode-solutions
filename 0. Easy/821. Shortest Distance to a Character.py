from typing import List


class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        list1: list = []
        list2: list = []
        for i in range(len(s)):
            if s[i] == c:
                list1.append(i)
        for i in range(len(s)):
            c = []
            for j in list1:
                c.append(abs(i - j))
            list2.append(min(c))
        return list2
