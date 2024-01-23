class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        cur = 0
        prev = None
        for car in s:
            if car == " ":
                if prev != " ":
                    last: int = cur
                    cur = 0
            else:
                cur += 1
            prev: str = car
        return last if not cur else cur
