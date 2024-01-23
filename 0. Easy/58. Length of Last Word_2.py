from typing import Literal


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        word: Literal[''] = ""

        for i in range(len(s) - 1, -1, -1):
            if s[i] == " ":
                if word:
                    return len(word)
            else:
                word += s[i]

        return len(word)
