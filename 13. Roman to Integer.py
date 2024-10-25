class Solution:
    def romanToInt(self, s: str) -> int:
        romanLetters = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}

        sum = 0
        i = 0
        while i < len(s):
            if i < len(s)-1 and romanLetters[s[i]] < romanLetters[s[i+1]]:
                sum += romanLetters[s[i+1]] - romanLetters[s[i]]
                i += 1
            else:
                sum += romanLetters[s[i]]
                i += 1

        return sum
