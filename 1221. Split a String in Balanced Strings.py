class Solution:
    def balancedStringSplit(self, s: str) -> int:
        sCount, count = 0, 0
        for i in range(len(s)):
            if s[i] == "R":
                sCount += 1
            elif s[i] == "L":
                sCount -= 1
            if sCount == 0:
                count += 1
        return count
