class Solution:
    def isHappy(self, n: int) -> bool:
        def find_sum_squares(num):
            curr_sum=0
            num_as_str = str(num)
            for char in num_as_str:
                curr_sum+= int(char)**2
            return curr_sum
               
        num_hash = {}
        while True:
            n = find_sum_squares(n)
            if n == 1:
                return True
            if n in num_hash:
                return False
            else:
                num_hash[n] = True
