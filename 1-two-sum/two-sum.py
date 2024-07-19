class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        Map = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in Map:
                return [Map[diff],i]
            Map[nums[i]] = i

        
        