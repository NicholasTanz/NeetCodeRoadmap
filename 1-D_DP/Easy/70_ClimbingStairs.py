class Solution:
    def climbStairs(self, n: int, memo={}) -> int:
        two, one = 1, 1
        for i in range(n - 1):
            temp = one
            one += two
            two = temp
        
        return one 
