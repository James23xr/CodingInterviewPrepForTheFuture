class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = 1
        postfix = 1
        ans = [1] * len(nums)
        for i in range(len(nums)):
            ans[i] = prefix
            prefix *= nums[i]
        for i in range(len(nums)-1,-1,-1):
            ans[i]*=postfix
            postfix *= nums[i]
        return(ans)
        