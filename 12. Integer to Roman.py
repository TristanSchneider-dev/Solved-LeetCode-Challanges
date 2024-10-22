class Solution:
    def intToRoman(self, num: int) -> str:
        romanValue = [
                    (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
                    (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
                    (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")
                ]

        romanString = ''

        for key, chars in romanValue:
            while num >= key:
                romanString += chars
                num -= key
        return romanString
