class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        nums1.sort()
        nums2.sort()
        i = j = 0
        res = []
        while i<len(nums1) and j<len(nums2):
            if nums1[i] < nums2[j]:
                i+=1
            elif nums1[i] > nums2[j]:
                j+=1
            else:
                if not res or res[-1] != nums1[i]:
                    res.append(nums1[i])
                i+=1
                j+=1
        return res
                