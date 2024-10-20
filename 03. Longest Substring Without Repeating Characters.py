class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seqList = []
        for index, tail in enumerate(s):
            seqString = ""
            for head in s[index:]:
                if head not in seqString: seqString += head
                else: break
            seqList.append(seqString)

        maxLen = 0
        for i in seqList:
            if len(i) > maxLen: maxLen = len(i)
        return maxLen
