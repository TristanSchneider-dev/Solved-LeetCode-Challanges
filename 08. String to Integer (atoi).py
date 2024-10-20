class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip()  # Entfernt führende Leerzeichen
        if len(s) == 0:
            return 0
        
        isNeg = False
        index = 0
        if s[0] == "-": 
            isNeg = True
            index = 1
        if s[0] == "+": 
            isNeg = False
            index = 1

        sAsString = 0
        while index < len(s) and s[index].isdigit():
            sAsString = sAsString * 10 + int(s[index])
            index += 1
        
        if isNeg: sAsString *= -1

        if sAsString > 2**31 - 1:
            sAsString = 2**31 - 1
        if sAsString < -2**31:
            sAsString = -2**31

        return sAsString
