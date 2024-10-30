class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i,e in enumerate(nums):
            diff = target - e
            if diff in seen:
                return [seen[diff],i]
            seen[e] = i
        
        