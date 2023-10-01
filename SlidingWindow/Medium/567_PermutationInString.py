class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_len = len(s1)
        s2_len = len(s2)
        if(s2_len < s1_len):
            return False
        
        # assign all chars in s1 to dict
        chars_in_s1 = {}
        for char in s1:
            if char in chars_in_s1:
                chars_in_s1[char]+=1
            else:
                chars_in_s1[char]=1
        
        l_idx, r_idx = 0, 0

        copy_chars_in_s1 = {key:value for key, value in chars_in_s1.items()}
        while(r_idx != s2_len and s2_len - l_idx >= s1_len):
           # if char in s2, is in dict reprsenting all chars in s1
            if(s2[r_idx] in copy_chars_in_s1):
               # if char hasn't been all used up
               if(copy_chars_in_s1[s2[r_idx]] > 0):
                    copy_chars_in_s1[s2[r_idx]]-=1
                    r_idx+=1
               else:
                    copy_chars_in_s1 = {key:value for key, value in chars_in_s1.items()}
                    l_idx+=1
                    r_idx=l_idx
               if(r_idx - l_idx == s1_len):
                    return True
            
            #char in s2 is not present in dict reprsenting all chars in s1
            else:
                if(l_idx != r_idx):
                    copy_chars_in_s1 = {key:value for key, value in chars_in_s1.items()}
                l_idx+=1
                r_idx=l_idx
        return False



