class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [0]
        for i in range(1, n + 1):
            cur = 0
            while i:
                cur += i & 1
                i >>= 1
            ans.append(cur)
        return ans


class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [0]
        for i in range(1, n+1):
            if i % 2 == 1:
                dp.append(dp[i-1]+1)
            else:
                dp.append(dp[i//2])
        return dp
