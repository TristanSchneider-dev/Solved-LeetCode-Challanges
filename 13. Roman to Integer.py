class Solution:
    def romanToInt(self, s: str) -> int:
        romanLetters = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}

        i, total = 0, 0
        while i < len(s)-1:
            if romanLetters[s[i]] >= romanLetters[s[i+1]]:
                total += romanLetters[s[i]]
                i += 1
            else:
                total -= romanLetters[s[i]]
                i += 1
        
        return total + romanLetters[s[-1]]
