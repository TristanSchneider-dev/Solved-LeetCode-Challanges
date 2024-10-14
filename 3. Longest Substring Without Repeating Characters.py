class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #all possible substring approach
        charsOfString = []
        for char in s:
            if char in charsOfString: continue
            charsOfString.append(char)

        #algorithmic approach
        possibleCombos = []
        currentString = ""
        for tail in s:
            firstIteration = False
            for head in s:
                if head == tail and firstIteration:
                    break
                currentString += head
                firstIteration = True
            possibleCombos.append(currentString)
            currentString = ""
        print(possibleCombos)
        #"abcabcbb"
        #['abc', 'a', 'ab', 'abc', 'a', 'ab', 'a', 'a']
        
