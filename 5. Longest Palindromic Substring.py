class Solution:
    def longestPalindrome(self, s: str) -> str:
        palindromes = []

        for i in range(len(s)):
            subString = ()
            for j in range(i+1, len(s)):
                if s[i] == s[j]: subString = (i, j)
            print(subString)
