from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        res = set()
        
        for n in range(len(nums)):
            i: int = n + 1
            j: int = len(nums) - 1
            
            while i < j:
                summ: int = nums[n] + nums[i] + nums[j]
                
                if summ == 0:
                    res.add((nums[n], nums[i], nums[j]))
                    i = i + 1
                    j = j - 1
                    
                elif summ > 0:
                    j = j - 1
                    
                elif summ < 0:
                    i = i + 1
                    
        return res
