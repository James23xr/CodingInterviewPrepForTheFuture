class Solution:
    def isNumber(self, s: str) -> bool:
        s = s.strip()  # Trim any whitespace from the ends
        n = len(s)
        
        has_num = False       # To ensure at least one digit
        has_decimal = False   # To allow only one decimal point before 'e' or 'E'
        has_exponent = False  # To allow only one 'e' or 'E'
        
        for i in range(n):
            char = s[i]
            
            if char.isdigit():
                has_num = True
                
            elif char in ['+', '-']:
                # Sign can only appear at the start or immediately after 'e' or 'E'
                if i > 0 and s[i - 1] not in ['e', 'E']:
                    return False
                    
            elif char == '.':
                # Decimal point can only appear before the exponent and must appear once
                if has_decimal or has_exponent:
                    return False
                has_decimal = True
                
            elif char in ['e', 'E']:
                # Exponent can only appear once and only if there has been a number before it
                if has_exponent or not has_num:
                    return False
                has_exponent = True
                has_num = False  # Reset has_num to ensure there are digits after 'e'
                
            else:
                # If the character is anything else, it's invalid
                return False
        
        return has_num
