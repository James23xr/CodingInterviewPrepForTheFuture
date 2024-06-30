class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        count = {}
        mostf = 0
        mostfe = -1
        for n in nums:
            if n%2 == 0: 
                count[n] = 1+ count.get(n,0)
                if count[n] >mostf:
                    mostf = count[n]
                    mostfe = n
                elif count[n] == mostf:
                    mostfe = min(n,mostfe)
        return mostfe

        