class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s): return s
        
        matrix = [[] for i in range(numRows)]
        
        counter = 0
        correction = 1
        for char in s:
            matrix[counter].append(char)
            if counter == 0:
                correction = 1
            if counter == (numRows - 1):
                correction = -1
            counter += correction

        collector = ""
        for i in range(numRows):
            for j in range(len(matrix[i])):
                collector += matrix[i][j]
        return collector
