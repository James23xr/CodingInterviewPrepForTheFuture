class Solution:
    def integerReplacement(self, n):
        counter = 0
        if n == 1:
            return counter
        elif n % 2 == 0:
            
            return 1+ self.integerReplacement(n/2)
        elif n % 2 != 0:
            
            return 1 + min(self.integerReplacement(n+1),self.integerReplacement(n-1))


  