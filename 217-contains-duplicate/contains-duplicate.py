class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set() #
        for num in nums: #iteration through nums array
            if num in seen: 
                return True
            seen.add(num) #add number to seen set
        return False
        