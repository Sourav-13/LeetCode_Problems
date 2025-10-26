class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        absTotal = 0
        for i in range(len(s)):
            absTotal += abs(i - t.find(s[i]))
        return absTotal
