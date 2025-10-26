class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxCandy = max(candies)
        ansList = []
        for candy in candies:
            if (candy + extraCandies) >= maxCandy:
                ansList.append(True)
            else:
                ansList.append(False)
        return ansList