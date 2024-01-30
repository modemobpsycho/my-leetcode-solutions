from typing import Any


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        st, res = 0, 0
        seen: set = {}

        for i, letter in enumerate(s):
            if seen.get(letter, -1) >= st:
                st: Any = seen[letter] + 1
            res: int = max(res, i - st + 1)
            seen[letter] = i

        return res
