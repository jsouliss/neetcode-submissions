class Solution:
    def isValid(self, s: str) -> bool:
        flag = False
        if len(s) >= 0:
            stack = []
            for char in s:
                if char == '[' or char == '{' or char == '(':
                    stack.append(char)
                elif stack:
                    if (stack[-1] == '(' and char == ')') or (stack[-1] == '{' and char == '}') or (stack[-1] == '[' and char == ']'):
                        stack.pop()
                    else:
                        return flag
                else:
                    return flag
            if not stack:
                flag = True
        return flag