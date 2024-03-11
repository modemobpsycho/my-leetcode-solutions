class Solution:
    def customSortString(self, order: str, s: str) -> str:
        res: list = ""
        for i in order:
            if i in set(s):
                res += i * s.count(i)
        for i in s:
            if i not in set(res):
                res += i * s.count(i)
        return res
