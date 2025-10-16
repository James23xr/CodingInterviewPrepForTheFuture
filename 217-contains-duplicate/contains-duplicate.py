class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen_elements = set()
        for num in nums:
            if num in seen_elements:
                return True
            seen_elements.add(num)
        return False
