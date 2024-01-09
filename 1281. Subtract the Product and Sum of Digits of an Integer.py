class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        p,s = 1,0
        while(n!=0):
            d = n%10
            p *= d
            s += d
            n = int(n/10)
        return p-s



#Alt solu ->
"""
class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        sNum = str(n)
        prod = 1
        sm = 0

        for i in sNum:
            prod *= int(i)
            sm += int(i)
        
        return prod - sm
        """