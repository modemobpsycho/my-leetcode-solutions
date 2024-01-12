class Solution:
    def findNumbers(self, nums: List[int]) -> int:

        def helper(num):
            ret = 0
            while (num):
                num //= 10
                ret += 1
            return ret

        ans = 0

        for num in nums:
            ans += 0 if helper(num) % 2 else 1

        return ans
