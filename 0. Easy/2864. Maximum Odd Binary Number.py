class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        return "".join(sorted(s)[-2::-1]) + "1"
