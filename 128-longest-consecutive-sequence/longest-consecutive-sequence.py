class Solution:
  def longestConsecutive(self, nums: List[int]) -> int:
    set_nums = set(nums)
    maxlength = 0

    for n in nums:
      if (n-1) not in set_nums:
        length = 0
  
        while(n+length) in set_nums:  # keeps going until seq is complete
          length+=1

        maxlength = max(maxlength,length)
        
    return maxlength
      
    