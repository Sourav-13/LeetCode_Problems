class Solution:
    def isPalindrome(self, x: int) -> bool:
        org_num = x
        if x < 0:
            return False
        rev_num= 0
        while x != 0:
            rev_num = rev_num*10 + x % 10
            x //= 10
            
        return rev_num == org_num

