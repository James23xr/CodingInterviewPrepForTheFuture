"""
nums = [2,7,11,15]
        |
        diff = target - num
        if diff in hashmap
        then we can return [i,hashmap[diff]]
        2:0
        7:1
        11:2
        15:3
target = 9
return indices of two nums that add up to target

"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for index,number in enumerate(nums):
            diff = target - number
            if diff in seen:
                return [index,seen[diff]]
            seen[number] = index
        
        