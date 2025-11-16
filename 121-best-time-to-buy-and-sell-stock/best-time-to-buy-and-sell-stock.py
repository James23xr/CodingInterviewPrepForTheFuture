class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_prof = 0
        min_p = prices[0]
        for i in range(len(prices)):
            min_p = min(min_p,prices[i])
            max_prof = max(max_prof,prices[i]-min_p)
        return max_prof
        