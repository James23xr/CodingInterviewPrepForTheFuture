class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = 0
        for r in range(len(nums)):
            if len(nums) <=1:
                return nums
            if nums[r] == 0:
                continue
            elif nums[r] != 0:
                nums[l], nums[r] = nums[r],nums[l]
                l+=1             
        return nums
        