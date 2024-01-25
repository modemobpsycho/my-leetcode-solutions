from typing import Literal


class Solution:
    def longestPalindrome(self, s: str) -> str:
        ans: Literal[""] = ""

        for i in range(len(s)):
            l, r: int = i, i

            while l >= 0 and r < len(s) and l <= r:
                if s[l] != s[r]:
                    break
                if r - l + 1 > len(ans):
                    ans = s[l : r + 1]

                l -= 1
                r += 1

            l, r: int = i, i + 1

            while l >= 0 and r < len(s) and l <= r:
                if s[l] != s[r]:
                    break
                if r - l + 1 > len(ans):
                    ans = s[l : r + 1]

                l -= 1
                r += 1
        return ans
