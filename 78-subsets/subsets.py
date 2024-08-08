class Solution:
  def subsets(self, nums: List[int]) -> List[List[int]]:
    res = []
    def backtracking(index, value):
      if index > len(nums):
        return
      res.append(list(value))
      for i in range(index, len(nums)):
        backtracking(i + 1, value + [nums[i]])
    backtracking(0, [])
    return res
