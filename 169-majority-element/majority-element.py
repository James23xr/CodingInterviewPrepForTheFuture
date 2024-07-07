class Solution:
    def majorityElement(self, ns: List[int]) -> int:
        r = 0
        c = 0
        for n in ns:
            if c == 0 or n == r:
                c += 1
                r = n
            elif n != r:
                c -= 1
        return r

 

