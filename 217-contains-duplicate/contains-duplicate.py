class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = {}
        for num in nums:
            if num not in seen:
                seen[num] = 1
            elif num in seen:
                return True
        return False
        