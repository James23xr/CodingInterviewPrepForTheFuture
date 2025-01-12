class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:   
        stack = []
        prev_freq = None
        for word in words:
            freq = tuple([word.count(char) for char in 'abcdefghijklmnopqrstuvwxyz'])
            if freq != prev_freq:
                stack.append(word)
                prev_freq = freq  
        return stack
            