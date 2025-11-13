class Solution:
    def getFactors(self, n: int) -> List[List[int]]:
        result = []
        def helper(n,start,path):
            for factor in range(start,int(n**0.5)+1):
                if n % factor == 0:
                    quotient = n // factor
                    result.append(path+[factor,quotient])
                    helper(quotient,factor,path+[factor])
        helper(n,2,[])
        return result
        