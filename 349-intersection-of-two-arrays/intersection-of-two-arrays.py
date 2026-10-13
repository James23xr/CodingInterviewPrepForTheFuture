class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        if len(nums1) > len(nums2):
            nums1,nums2 = nums2,nums1
        small = set(nums1)
        res = []
        for num in nums2:
            if num in small:
                res.append(num)
                small.remove(num)
        return res
        