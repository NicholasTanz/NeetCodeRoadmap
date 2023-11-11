class Solution:
    def hammingWeight(self, n: int) -> int:
        num_1s = 0
        while(n / 2 != 0):
            num_1s += n % 2
            n//=2
        
        return num_1s
