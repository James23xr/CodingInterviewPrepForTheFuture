class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        Map = {}
        for i,e in enumerate(nums):
            diff = target - nums[i]
            if diff in Map:
                return [Map[diff],i]
            Map[e] = i
        