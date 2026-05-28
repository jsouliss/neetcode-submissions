class Solution:
    def isValid(self, s: str) -> bool:
        op = { ')':'(', '}':'{', ']':'[' }
        my_stack = []
        for i in range(len(s)):
            if s[i] in op and my_stack:
                if op[s[i]] == my_stack[-1]:
                    my_stack.pop()
                else:
                    return False
            else: 
                my_stack.append(s[i])

        return not my_stack