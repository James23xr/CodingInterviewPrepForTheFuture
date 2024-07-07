class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        r = 0
        c = 0
        for n in nums:
            if c == 0 or n == r:
                c += 1
                r = n
            elif n != r:
                c -= 1
        return r

 

