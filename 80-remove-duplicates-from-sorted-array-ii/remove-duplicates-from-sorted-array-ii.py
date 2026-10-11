class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        write = 0
        for i in range(len(nums)):
            if write<2 or nums[i] != nums[write-2]:
                nums[write] = nums[i]
                write+=1
        return write
        