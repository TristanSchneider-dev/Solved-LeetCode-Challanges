class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs: return ''
        
        shortestLength = len(min(strs, key=len))
        commonPrefix = ''
        for index in range(shortestLength):
            char = strs[0][index]
            if all(s[index] == char for s in strs):
                commonPrefix += char
            else:
                break
                
        return commonPrefix
