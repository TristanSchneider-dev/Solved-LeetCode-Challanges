class Solution:
    def intToRoman(self, num: int) -> str:
        romanValue = {1:'I', 5:'V', 10:'X', 50:'L', 100:'C', 500:'D', 1000:'M'}
        
        romanString = ''
        while num > 0:
            if num > 1000:
                romanString += 'M'
                num -= 1000
            elif num > 500:
                romanString += 'D'
                num -= 500
            elif num > 100:
                romanString += 'C'
                num -= 100
            elif num > 50:
                romanString += 'L'
                num -= 50
            elif num > 10:
                romanString += 'X'
                num -= 10
            elif num > 5:
                romanString += 'V'
                num -= 5
            else:
                romanString += 'I'
                num -= 1

        return romanString