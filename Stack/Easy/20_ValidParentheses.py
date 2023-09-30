class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            # add open brackets to stack
            if(char == '(' or char == '{' or char == '['):
                stack.append(char)
            # assert last element in stack matches with closed bracket
            else:
                # stack can't be empty if close bracket found; else false
                if(len(stack) == 0): 
                    return False
                elif(char == ')'):
                    if(stack[-1] != '('):
                        return False
                elif(char == ']'):
                    if(stack[-1] != '['):
                        return False
                else:
                    if(stack[-1] != '{'):
                        return False
                del stack[-1]
        
        return True if len(stack)==0 else False
