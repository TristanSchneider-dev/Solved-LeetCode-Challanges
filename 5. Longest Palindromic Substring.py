class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expandAroundCenter(left: int, right: int) -> str:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1:right]

        if len(s) <= 1:
            return s
        
        longest_palindrome = ""

        for i in range(len(s)):
            #(single center character)
            odd_palindrome = expandAroundCenter(i, i)
            #(center between two characters)
            even_palindrome = expandAroundCenter(i, i + 1)
            
            longest_palindrome = max(longest_palindrome, odd_palindrome, even_palindrome, key=len)
        
        return longest_palindrome
