class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        max_seq = 0 
        for num in numset:
            if num - 1 not in numset: 
                cur_seq_len = 1
                temp = num
                while temp+1 in numset:
                    cur_seq_len += 1
                    temp += 1
                
                max_seq = max(max_seq, cur_seq_len) 
        return max_seq
