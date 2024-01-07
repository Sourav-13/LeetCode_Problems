class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        count = 0
        l = len(jewels)
        for i in range(l):
            count += stones.count(jewels[i])
        return count