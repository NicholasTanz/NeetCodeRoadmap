class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        #edge case of 1 num - just return
        if(len(tokens) == 1):
            return int(tokens[0])
        num_stack = []
        for val in tokens:
            if val == '*':
                num_stack.append(num_stack.pop() * num_stack.pop()) 
            elif val == '+':
                num_stack.append(num_stack.pop() + num_stack.pop()) 
            elif val == '-':
                num_stack.append(num_stack.pop(-2) - num_stack.pop()) 
            elif val == '/':
                curr_val = abs(int(num_stack[-2])) // abs(int(num_stack[-1])) 
                negative_val = True if int(num_stack[-2]) < 0 and int(num_stack[-1]) > 0 or int(num_stack[-2]) > 0 and int(num_stack[-1]) < 0 else False
                num_stack.pop()
                num_stack.pop()
                if(negative_val):
                    num_stack.append(-1 * curr_val)
                else:
                    num_stack.append(curr_val) 
            else:
                num_stack.append(int(val))

        return num_stack[-1]
