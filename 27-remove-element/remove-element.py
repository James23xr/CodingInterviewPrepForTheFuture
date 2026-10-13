class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        k = 0
        for read in range(len(nums)):
            if nums[read] != val:
                nums[k] = nums[read]
                k+=1
        return k
        