class Solution:
    def search(self, nums: list[int], target: int) -> int:
        lo, hi = 0, len(nums)
        while lo<hi:
            mid = (lo+hi) // 2
            if nums[mid] >= target:
                hi = mid
            else:
                lo = mid + 1
        if lo < len(nums) and nums[lo] == target:
            return lo
        return -1
        