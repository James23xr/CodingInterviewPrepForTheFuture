class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i, e in enumerate(nums):
            if i > 0  and nums[i-1] == e:
                continue
            l,r = i+1,len(nums)-1
            while l < r:
                if e + nums[l] + nums[r] > 0:
                    r-=1
                elif e + nums[l] + nums[r] < 0:
                    l+=1
                else:
                    res.append([e,nums[l],nums[r]])
                    l+=1
                    while nums[l] == nums[l-1] and l<r:
                        l+=1
        return res



        