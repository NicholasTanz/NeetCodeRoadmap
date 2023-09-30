class Solution:
    def isPalindrome(self, s: str) -> bool:
        l_p, r_p = 0, len(s)-1
        while(l_p < r_p):
            # find nxt char or num
            while(not s[l_p].isalnum() and r_p > l_p):
                l_p+=1
            while(not s[r_p].isalnum() and r_p > l_p):
                r_p-=1
            # check to make sure char matches for lower & upper idx; else can't be palindrome. 
            if(s[l_p].lower() != s[r_p].lower()):
                return False
            l_p+=1
            r_p-=1
        return True
