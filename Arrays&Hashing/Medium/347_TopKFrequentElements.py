class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        find_freq = {}

        # find nums of occurences for each val in nums
        for num in nums:
            if(num in find_freq):
                find_freq[num]+=1
            else:
                find_freq[num] = 1

       # assign num of occurences in order to ret_list ; higher occurence = higher_idx
        ret_list = [-1] * (len(nums)  + 1)
        for key, val in find_freq.items():
            if(ret_list[val] == -1):
                ret_list[val] = [key]
            else:
                ret_list[val].append(key)


        # find k most frequent elements - start from back of ret_list 
        ret_list_ = []
        count=0
        idx=0
        while(count != k):
            if(ret_list[len(nums) - 1 - idx] != -1):
                count+=len(ret_list[len(nums)-1-idx])
                for val in ret_list[len(nums)-1-idx]:
                    ret_list_.append(val)
            idx+=1

        return ret_list_

            
