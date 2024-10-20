class Solution:
    def maxArea(self, height: List[int]) -> int:
        areaValues= []
        distance = 0
        for index, i in enumerate(height):
            distance = 0
            for j in height[index+1:]:
                distance += 1
                areaValues.append(min(i, j) * distance)

        return max(areaValues)

