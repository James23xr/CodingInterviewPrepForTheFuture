class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        seen = {}
        counter = 0
        for i in range(len(nums)):
            seen[nums[i]] = i
        for num in nums:
            if (num + diff) in seen and (num + diff+diff) in seen:
                counter += 1
        return counter


        