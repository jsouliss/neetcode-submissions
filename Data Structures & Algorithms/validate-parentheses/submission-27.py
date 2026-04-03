class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) >= 0:
            stack = []
            for char in s:
                if char == '[' or char == '{' or char == '(':
                    stack.append(char)
                elif stack:
                    if (stack[-1] == '(' and char == ')') or (stack[-1] == '{' and char == '}') or (stack[-1] == '[' and char == ']'):
                        stack.pop()
                    else: 
                        return False
                else:
                    return False

            if not stack:
                return True
            else:
                return False
        else:
            return False