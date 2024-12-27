class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        #last index of array nums1
        last_index = m + n -1
        #merge arrays in reverse order
        while m > 0 and n > 0:
            if nums1[m-1] > nums2[n-1]:
                nums1[last_index] = nums1[m-1]
                m-=1
            else:
                nums1[last_index] = nums2[n-1]
                n-=1
            last_index -=1
        #adding leftover nums2 elements to nums1
        while n > 0:
            nums1[last_index] = nums2[n-1]
            n -=1
            last_index -= 1

        