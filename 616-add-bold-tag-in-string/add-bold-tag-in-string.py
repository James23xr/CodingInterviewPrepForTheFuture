class Solution:
    def addBoldTag(self, s: str, words: List[str]) -> str:
        n = len(s)
        bold_status = [False] * n
        for word in words:
            start = s.find(word)
            while start != -1:
                for i in range(start,start+len(word)):
                    bold_status[i] = True
                start = s.find(word,start+1)
        open_tag = '<b>'
        close_tag = '</b>'
        result = []        
        for i in range(len(s)):
            if bold_status[i] and (i==0 or not bold_status[i-1]):
                result.append(open_tag)
            result.append(s[i])
            if bold_status[i] and(i==n-1 or not bold_status[i+1]):
                result.append(close_tag)
        return ''.join(result)

        