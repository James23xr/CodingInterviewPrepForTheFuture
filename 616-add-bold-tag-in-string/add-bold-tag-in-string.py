class Solution:
    def addBoldTag(self, s: str, words: List[str]) -> str:
        n = len(s)
        bold = [False] * n # if s ='abcxyz123' bold = 9 False statements in an array [F,F,F,F,F,F,F,F]
        for i in range(n):
            for word in words:
                if s.startswith(word,i):
                    for j in range(i,min(i+len(word),n)):
                        bold[j] = True
            result = []
        i = 0
        while i < n:
            if bold[i]:
                # Start of a bold section
                result.append("<b>")
                while i < n and bold[i]:
                    result.append(s[i])
                    i += 1
                result.append("</b>")
            else:
                # Non-bold character
                result.append(s[i])
                i += 1
        
        return "".join(result)



        