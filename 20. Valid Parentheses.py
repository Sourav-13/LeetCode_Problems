class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        s_dic = { ')' : '(',
                '}' : '{',
                ']' : '['
                }
        
        for i in range(len(s)):
            if s[i] in "({[":
            # if (s[i] == '(' or s[i] == '{' or s[i] == '['):
                stack.append(s[i])
            else:
                if not stack or s_dic[s[i]] != stack[-1]:
                    return False
                stack.pop()
                    
        if not stack:
            return True
        else:
            return False