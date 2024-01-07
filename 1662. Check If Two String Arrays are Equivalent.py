class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        s1,s2= "",""
        for w1 in word1:
            s1 += w1
        for w2 in word2:
            s2 += w2
        if s1 == s2:
            return True
        else:
            return False
