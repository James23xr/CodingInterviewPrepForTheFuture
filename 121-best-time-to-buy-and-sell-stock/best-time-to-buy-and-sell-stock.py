class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l,r = 0,1
        MaxProfit = 0
        while r < len(prices):
            if prices[r] > prices[l]:
                profit = prices[r] - prices[l]
                MaxProfit = max(profit,MaxProfit)
                r+=1
                
            else:
                l = r
                r+=1
        return MaxProfit
        