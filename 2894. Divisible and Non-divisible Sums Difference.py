class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        num1, num2 = 0, 0
        for i in range(n):
            if (i + 1) % m != 0:
                num1 += i + 1
            else:
                num2 += i + 1
        return num1 - num2
