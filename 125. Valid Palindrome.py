import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = re.sub(r'[^a-z0-9]', '', s)
        size = len(s) 
        rev_i = size -1

        for i in range(size//2):
            if (s[i] != s[rev_i]):
                return False
            rev_i -=1
        return True
    
    
# 0 ms
class Solution:
    def isPalindrome(self, s: str) -> bool:
       newStr = ''.join(filter(str.isalnum, s.lower()))
       return newStr==newStr[::-1]
   

            