class Solution:
    def maxArea(self, height: List[int]) -> int:
        biggestArea = 0

        leftEnd = 0
        rightEnd = len(height)-1
        while leftEnd < rightEnd:
            distance = rightEnd - leftEnd
            area = min(height[leftEnd], height[rightEnd]) * distance
            if area > biggestArea: biggestArea = area
            
            if height[leftEnd] < height[rightEnd]: leftEnd += 1
            else:rightEnd -= 1

        return(biggestArea)
