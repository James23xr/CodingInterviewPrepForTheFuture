class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        Map = {}
        for i,n in enumerate(nums):
            diff = target - n
            if diff in Map:
                return [i,Map[diff]]
            Map[n] = i
        return False


        