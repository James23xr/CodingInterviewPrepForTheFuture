class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        s = s.upper()
        s = s.replace("-","")
        s = s[::-1]
        res = []
        for i in range(0,len(s),k):
            res.append(s[i:i+k])
        return "-".join(res)[::-1]
        