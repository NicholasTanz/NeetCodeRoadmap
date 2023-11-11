class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        int_ = 0
        len_digits = len(digits) - 1
        for idx, val in enumerate(digits):
            int_ += (10**(len_digits - idx) * val)
        
        int_+=1
        idx = len_digits
        idx = 0
        while int_ > 0:
            if(len_digits - idx < 0):
                digits.insert(0, 1)
                break
            else:
                digits[len_digits - idx] = int_ % 10
            int_ = int_ // 10
            idx+=1

        return digits
