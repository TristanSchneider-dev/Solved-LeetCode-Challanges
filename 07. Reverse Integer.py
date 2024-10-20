class Solution:
    def reverse(self, x: int) -> int:
        def multiplier(x) -> int:
            digits = len(str(x))
            return 10 ** (digits - 1)

        negFlag = False
        if x < 0: 
            x = abs(x)
            negFlag = True

        reversedInt = 0
        while x != 0:
            reversedInt += ((x % 10) * multiplier(x))
            x = x // 10

        if reversedInt > 2**31 - 1: #Overflow protection
            return 0

        if negFlag: return reversedInt * -1
        else: return reversedInt
