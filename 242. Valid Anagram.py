class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        from collections import defaultdict

        if len(s) != len(t):
            return False

        dict_s = defaultdict(int)
        dict_t = defaultdict(int)

        for i in range (len(s)):
            dict_s[s[i]] +=1
            dict_t[t[i]] +=1

        for i in range (len(s)):
            if s[i] not in dict_t or dict_s[s[i]] != dict_t[s[i]]:
                return False
        return True


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        # my_set = set(s)
    
        for l in s:
            if s.count(l) != t.count(l):
                return False
        return True
    
    
#better

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        a = Counter(s)
        b = Counter(t)
        return a==b
    
    