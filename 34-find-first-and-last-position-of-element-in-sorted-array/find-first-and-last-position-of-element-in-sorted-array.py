class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def binSearch(nums,target,leftbias):
            l = 0
            r = len(nums)-1
            i =-1
            while l<=r:
                m = (l+r)//2
                if nums[m] < target:
                    l = m +1
                elif nums[m] > target:
                    r = m-1
                else:
                    i=m
                    if leftbias:
                        r = m-1
                    else:
                        l = m+1
            return i  
        left= binSearch(nums,target,True)
        right= binSearch(nums,target,False)
        return [left,right]


        