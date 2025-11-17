class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        spaces = k
        for i in range(len(nums)):
            if nums[i] ==1:
                if spaces <k:
                    return False
                spaces = 0
            else:
                spaces+=1
        return True