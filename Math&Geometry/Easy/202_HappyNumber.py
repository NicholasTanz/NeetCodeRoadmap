class Solution:
    def isHappy(self, n: int) -> bool:
        visitSet = set()

        def squareDigits(num):
            str_num = str(num)
            square_sum = 0
            for char in str_num:
                square_sum += int(char)**2

            return square_sum

        while n != 1:
            visitSet.add(n)
            n = squareDigits(n)
            if(n in visitSet):
                return False

        return True
