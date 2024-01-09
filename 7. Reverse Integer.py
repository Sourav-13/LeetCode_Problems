class Solution:
    def reverse(self, x: int) -> int:
        c = x
        x = abs(x)
        revNum =0
        while(x!=0):
            d = x%10
            revNum = revNum*10 + d
            x = int(x/10)
        if(c<0):
            revNum = -revNum
        if(revNum>2147483647 or revNum<-2147483648):
            return 0
        return revNum