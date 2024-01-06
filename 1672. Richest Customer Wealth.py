class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        wealth = []
        l = len(accounts)
        for i in range(l):
            sum = 0
            for j in range(len(accounts[i])):
                sum += accounts[i][j]
            wealth.append(sum)
        return max(wealth)



#Better Solution ->
    """
    class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        wealth=[]
        for i in accounts:
            wealth.append(sum(i))
        return max(wealth)
    """