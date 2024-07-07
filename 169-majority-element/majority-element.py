class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        res = 0
        count = 0
        for num in nums:
            if count == 0 or num == res:
                count += 1
                res = num
            else:
                count -= 1
        return res

 

