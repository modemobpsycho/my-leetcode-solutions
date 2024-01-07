class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:

        cur = sum(nums[:k])
        cur_max = cur

        for i in range(k, len(nums)):
            cur -= nums[i - k]
            cur += nums[i]
            cur_max = max(cur, cur_max)

        return cur_max / k
