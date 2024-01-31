class Solution:
    def climbStairs(self, n: int) -> int:
        a, b = 1, 2
        for i in range(n - 1):
            a, b: int = b, a + b
        return a
