class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        normS, prevChar = '', '' #remove multi-* shit...
        for char in p:
            if char == '*' and prevChar == '*': continue
            normS += char
            prevChar = char

        sLen, pLen, lastP = len(s), len(p), '' #s should be always grater.. right?

        for sIndex in range(0, sLen):
            for pIndex in range(0, pLen):
                if sIndex <= pLen: #Index in range
                    if p[sIndex] == s[sIndex]: 
                        lastP = p[sIndex]
                        continue
                    else: return False
                    if p[sIndex] == '.': 
                        lastP = p[sIndex]
                        continue
                else: #!Index in range
                    return lastP == '*'
