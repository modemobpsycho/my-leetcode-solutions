class Solution:
    def reverseVowels(self, s: str) -> str:
        v = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}
        a = [f for f in s[::-1] if f in v]
        n = ""
        j = 0
        for i in s:
            if i in v:
                n += a[j]
                j += 1
            else:
                n += i

        return n
