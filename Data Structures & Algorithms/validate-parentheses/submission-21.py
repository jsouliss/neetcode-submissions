class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) >= 0 and len(s) % 2 == 0:
            stack = []
            for i in range(0, len(s)):
                if s[i] == '[' or s[i] == '{' or s[i] == '(':
                    stack.append(s[i])
                elif s[i] == ')' or s[i] == '}' or s[i] == ']':
                    if stack:
                        if stack[-1] == '(' and s[i] == ')' or stack[-1] == '{' and s[i] == '}' or stack[-1] == '[' and s[i] == ']':
                            stack.pop()
                        else:
                            return False
                    else:
                        return False
            if len(stack) == 0:
                return True
            else:
                return False
        else:
            return False