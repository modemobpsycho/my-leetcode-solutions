from typing import Counter


class Solution:
    def longestPalindrome(self, s: str) -> int:
        cnt = Counter(s)
        ans = 0

        for l, c in cnt.items():
            cur: int = c - (c % 2)
            ans += cur
            cnt[l] -= cur

        return ans if not sum(cnt.values()) else ans + 1
