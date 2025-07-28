class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = {}
        for i,e in enumerate(nums):
            if e in seen:
                return True
            seen[e] = i
        return False
        