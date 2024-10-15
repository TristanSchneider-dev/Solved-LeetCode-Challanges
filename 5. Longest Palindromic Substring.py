class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1: return s
        palindromes = []

        for i in range(len(s)-2):
            subString = ""
            if s[i] == s[i+2]:
                indexL = i
                indexR = i+2
                subString = s[i+1]
                while indexL >=0 and indexR <= len(s) and s[indexL] == s[indexR]:
                    subString = s[indexL] + subString + s[indexR]
                    palindromes.append(subString)
                    indexL -= 1
                    indexR += 1
        
        maxLength = 0
        maxLengthIndex = -1

        for index, pal in enumerate(palindromes):
            if len(pal) > maxLength: 
                maxLength = len(pal)
                maxLengthIndex = index
        return palindromes[maxLengthIndex]              
