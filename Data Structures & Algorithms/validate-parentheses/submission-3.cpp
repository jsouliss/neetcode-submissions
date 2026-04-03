class Solution {
public:
    bool isValid(string s) {
        bool flag = false;
        size_t length = s.length();
        stack<char> parStack;

        if(s[0] == ']' || s[0] == ')' || s[0] == '}') 
        {
            return false;
        }

        for (int i = 0; i < length; ++i)
        {
            if (s[i] == '[' || s[i] == '(' || s[i] == '{')
            {
            parStack.push(s[i]);
            }
            else if (s[i] == ']' || s[i] == ')' || s[i] == '}')
            {
                if(!parStack.empty()){
                    char top = parStack.top();
                    parStack.pop();
                    if (top == '{' && s[i] != '}' ||
                        top == '(' && s[i] != ')' ||
                        top == '[' && s[i] != ']')
                    {
                        return flag;
                    }
                }
            }
        }

        if (parStack.empty())
        {
            return true;
        }

        return flag;
    }
};
