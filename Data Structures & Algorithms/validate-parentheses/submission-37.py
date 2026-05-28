class Solution:
    def isValid(self, s: str) -> bool:
        my_stack = []
        for i in range(len(s)):
            match s[i]:
                case '(':
                    my_stack.append(s[i])
                case ')':
                    if my_stack:
                        if my_stack[-1] == '(':
                            my_stack.pop()
                        else: 
                            return False
                    else: 
                        return False
                case '{':
                    my_stack.append(s[i])
                case '}':
                    if my_stack:
                        if my_stack[-1] == '{':
                            my_stack.pop()
                        else:
                            return False
                    else: 
                        return False
                case '[':
                    my_stack.append(s[i])
                case ']':
                    if my_stack: 
                        if my_stack[-1] == '[':
                            my_stack.pop()
                        else: 
                           return False
                    else:
                       return False

        return not my_stack