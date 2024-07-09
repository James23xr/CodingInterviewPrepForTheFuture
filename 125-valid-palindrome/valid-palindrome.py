class Solution:
    def AlphaNum(self,c):
        return (ord("A")<= ord(c)<=ord("Z")or
                ord("a")<=ord(c)<=ord("z")or
                ord("0")<=ord(c)<=ord("9"))

    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s)-1
        while l <r:
            if not self.AlphaNum(s[l]):
                l+=1
            elif not self.AlphaNum(s[r]):
                r-=1
            else:
                if s[l].lower() != s[r].lower():
                    return False
                l +=1
                r-=1
        return True

    
    
        