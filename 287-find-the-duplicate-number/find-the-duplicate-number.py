class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        a = nums[0]
        b = nums[0]
        while True:
            a = nums[a]
            b = nums[nums[b]]
            if a == b:
                break
        b = nums[0]
        while b != a:
            a = nums[a]
            b = nums[b]
        return b