class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        l = 0
        r = len(numbers)-1
        while l<r:
            s = numbers[l] +numbers[r]
            if s == target:
                return [l+1,r+1]
            elif s < target:
                l+=1
            else:
                r-=1
        return
        