class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        N = len(nums)
        sorted_list = list(sorted(x *x for x in nums))
        return sum(sorted_list[N//2:]) - sum(sorted_list[:N//2]) 
        