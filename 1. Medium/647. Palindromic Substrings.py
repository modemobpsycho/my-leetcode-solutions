class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        ans = 0

        if n <= 0:
            return 0

        dp = [[False] * n for _ in range(n)]

        for i in range(n):
            dp[i][i] = True
            ans += 1

        for i in range(n - 1):
            dp[i][i + 1] = (s[i] == s[i + 1])
            ans += 1 if dp[i][i + 1] else 0

        for length in range(3, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                dp[i][j] = dp[i + 1][j - 1] and (s[i] == s[j])
                ans += 1 if dp[i][j] else 0

        return ans
