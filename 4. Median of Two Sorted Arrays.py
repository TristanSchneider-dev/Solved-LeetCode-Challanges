class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        mergedList = nums1 + nums2
        mergedList.sort()

        length = len(mergedList)
        if length % 2 == 1: return mergedList[length//2] #odd
        else: #even
            midR = mergedList[length//2]
            midL = mergedList[(length//2) - 1]
            return float((midR + midL) / 2)
