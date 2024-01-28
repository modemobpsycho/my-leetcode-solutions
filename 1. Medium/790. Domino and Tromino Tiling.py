class Solution:
    def numTilings(self, n: int) -> int:
        if n == 1:
            return 1
        dp: list[int] = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 1
        dp[2] = 2

        for i in range(3, n + 1):
            dp[i] = (2 * dp[i - 1] + dp[i - 3]) % (10**9 + 7)

        return dp[-1]
