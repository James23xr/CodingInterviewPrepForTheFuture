class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        n = len(nums)
        res = [0] * n
        l = 0
        r = n -1
        pos = n-1
        while l<=r:
            left_sq = nums[l] **2
            right_sq = nums[r] **2
            if left_sq > right_sq:
                res[pos] = left_sq
                l+=1
            else:
                res[pos] = right_sq
                r-=1
            pos-=1
        return res
        