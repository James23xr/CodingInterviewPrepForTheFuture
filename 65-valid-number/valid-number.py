class Solution:
    def isNumber(self, s: str) -> bool:
        s = s.strip()
        n = len(s)
        has_num = False
        has_dec = False
        has_exp = False
        for i in range(n):
            char = s[i]
            if char.isdigit():
                has_num = True
            elif char in ['+','-']:
                if i >0 and s[i-1] not in ['e','E']:
                    return False
            elif char == '.':
                if has_dec or has_exp:
                    return False
                has_dec =  True
            elif char in ['e','E']:
                if not has_num or has_exp:
                    return False
                has_exp = True
                has_num = False
            else:
                return False
        return has_num
        