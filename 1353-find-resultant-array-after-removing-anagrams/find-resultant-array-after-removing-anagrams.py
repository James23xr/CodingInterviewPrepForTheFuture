class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
            # Stack to hold the resultant words
        stack = []
        # To store the character frequency of the top word in the stack
        prev_freq = None

        for word in words:
            # Generate character frequency as a tuple
            freq = tuple([word.count(char) for char in 'abcdefghijklmnopqrstuvwxyz'])
            
            # Compare with the previous frequency
            if freq != prev_freq:
                stack.append(word)
                prev_freq = freq  # Update the previous frequency
        
        return stack
            