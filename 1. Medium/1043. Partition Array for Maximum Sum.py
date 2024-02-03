from typing import List


class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        n: int = len(arr)

        dp: list[int] = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            mx = 0
            for j in range(i, min(n, i + k)):
                mx: int = max(mx, arr[j])
                dp[i] = max(dp[i], mx * (j - i + 1) + dp[j + 1])
        return dp[0]
