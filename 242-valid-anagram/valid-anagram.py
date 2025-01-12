class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #anagram word formed by rearranging the characters of one word to form another word using all the original characters once
        if len(s) != len(t): # if string lengths are different it cannot be an anagram
            return False
        count = defaultdict(int) #defaultdict automates creation of key with value  of zero if key does not 
        for i in range(len(s)): #since they are same length we an use one length of one string to iterate through both
            count[s[i]] += 1 #increase char count by 1
            count[t[i]] -= 1 #decrease char count by 1
        for char in count: #go through dictionary
            if count[char] != 0:
                return False #cannot be anagram
        return True #all charcounts are 0
        