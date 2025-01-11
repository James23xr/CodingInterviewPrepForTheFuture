class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = [] # new array of length 2n
        n = len(nums) # size of old array
        for i in range(2): #size we want
            for i in range(n): #iteration through nums array
                ans.append(nums[i]) #adding current element to array ans
        return ans # returning new array after adding original array twice
        