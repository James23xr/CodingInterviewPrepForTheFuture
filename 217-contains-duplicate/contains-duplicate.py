class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for e in nums:
            if e in seen:
                return True
            seen.add(e)
        return False
        