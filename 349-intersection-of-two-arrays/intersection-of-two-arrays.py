class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        unique_nums1 = set(nums1)
        result = []
        for num in nums2:
            if num in unique_nums1:
                result.append(num)
                unique_nums1.remove(num)
        return result