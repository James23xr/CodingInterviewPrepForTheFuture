class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        res = 0
        count = 0
        for n in nums:
            if count == 0 or n == res:
                res = n
                count+=1
            elif n !=res:
                count-=1
        return res



