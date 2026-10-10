class Solution:
    def sortArrayByParity(self, nums: list[int]) -> list[int]:
        write = 0
        for read in range(len(nums)):
            if nums[read] % 2 ==0:
                nums[write],nums[read] = nums[read],nums[write]
                write+=1
        return nums
        