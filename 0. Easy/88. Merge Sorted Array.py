class Solution:
    def merge(self, nums1: listdir[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        for i in range(len(nums1)-m):
            nums1.remove(0)

        for i in range(len(nums2)-n):
            nums2.remove(0)

        print(nums1, nums2)

        nums1.extend(nums2)

        nums1.sort()

        return nums1
