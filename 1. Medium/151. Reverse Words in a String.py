class Solution:
    def reverseWords(self, s: str) -> str:
        x: list[str] = s.split()
        return " ".join(x[::-1])
