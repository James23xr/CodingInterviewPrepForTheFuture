class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = []
        n = len(nums)
        for i in range(2):
            for i in range(n):
                ans.append(nums[i])
        return ans
        