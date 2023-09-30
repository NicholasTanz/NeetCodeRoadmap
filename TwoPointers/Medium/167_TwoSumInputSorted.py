class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l_p, r_p = 0, len(numbers)-1

        while l_p < r_p:
            sum_ = numbers[l_p]+numbers[r_p]
            if(sum_ == target):
                return [l_p+1, r_p+1]
            elif(sum_ < target):
                l_p+=1
            else:
                r_p-=1
