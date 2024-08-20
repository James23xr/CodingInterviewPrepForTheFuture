class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote) > len(magazine): 
            return False 
        Map = {}
        for i in range(len(magazine)):
            Map[magazine[i]] = Map.get(magazine[i],0) + 1 
  
        for char in ransomNote:
            if char not in Map:
                return False
            if Map[char] == 0:
                return False
            Map[char] -= 1
        return True
                                    
                               
        